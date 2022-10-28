from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from Lobby.models import Lobby
from Stop.models import Property
from Users.models import User


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    properties = models.ManyToManyField(Property)

    class Meta:
        unique_together = ("lobby", "user")

    def clean(self, *args, **kwargs):
        if Player.objects.filter(lobby_id=self.lobby.id).count() == 4:
            raise ValidationError("Lobby can't have more than 4 players.")

        super().clean(*args, **kwargs)

    @property
    def is_bankrupt(self) -> bool:
        return self.money != 0.00 and self.properties.count() != 0
