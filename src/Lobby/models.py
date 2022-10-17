from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from Player.models import Player


class Lobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Lobbies"


class LobbyPlayer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def clean(self, *args, **kwargs):
        if LobbyPlayer.objects.filter(lobby_id=self.lobby.id).count() == 4:
            raise ValidationError("Lobby can't have more than 4 players.")

    class Meta:
        unique_together = ("lobby", "player")
