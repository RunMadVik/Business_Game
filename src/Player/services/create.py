from typing import Optional, Tuple, Union

from django.core.exceptions import ValidationError

from Lobby.models import Lobby
from Player.models import Player
from Users.models import User


def get_or_create_player(
    user: User, lobby: Lobby, money: Optional[int] = None, name: Optional[str] = None
) -> Tuple[bool, Union[str, Player]]:
    try:
        player = Player.objects.get(user=user, lobby=lobby)
    except Player.DoesNotExist:
        player = Player(
            user=user,
            lobby=lobby,
            money=money or lobby.starting_money,
            name=name or user.get_short_name(),
        )
        try:
            player.full_clean()
            player.save()
        except ValidationError as error:
            return False, str(error)

        return True, player

    return True, player
