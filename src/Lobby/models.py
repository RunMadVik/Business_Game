from uuid import uuid4

from django.db import models

from Users.models import User


class Lobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    starting_money = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Lobbies"
