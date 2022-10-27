from uuid import uuid4

from django.db import models

from Stop.models import Property
from Users.models import User


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    properties = models.ManyToManyField(Property)

    @property
    def is_bankrupt(self) -> bool:
        return self.money != 0.00 and self.properties.count() != 0
