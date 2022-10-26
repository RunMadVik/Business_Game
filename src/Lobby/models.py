from uuid import uuid4

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from Player.models import Player


class Lobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Lobbies"


class LobbyPlayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.player} in lobby {self.lobby}"

    def clean(self, *args, **kwargs):
        if LobbyPlayer.objects.filter(lobby_id=self.lobby.id).count() == 4:
            raise ValidationError("Lobby can't have more than 4 players.")

    class Meta:
        unique_together = ("lobby", "player")
