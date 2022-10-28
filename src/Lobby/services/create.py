from typing import Optional, Tuple, Union

from django.core.exceptions import ValidationError

from Lobby.helpers import generate_random_string
from Lobby.models import Lobby
from Player.models import Player
from Player.services import get_or_create_player
from Users.models import User


def get_or_create_lobby(
    user: User,
    name: Optional[str] = None,
    password: Optional[str] = None,
    starting_money: Optional[int] = None,
) -> Tuple[bool, Union[Lobby, str]]:
    try:
        if name:
            lobby = Lobby.objects.get(name=name, created_by=user)
            return True, lobby
    except Lobby.DoesNotExist:
        lobby = Lobby(
            name=name or generate_random_string(length=10),
            password=password or generate_random_string(length=10),
            starting_money=starting_money or 30000,
            created_by=user,
        )
        try:
            lobby.save()
        except ValidationError as error:
            return False, str(error)

        success, player = get_or_create_player(
            user=user, lobby=lobby, money=starting_money or 30000
        )
        if not success:
            return success, player

        return True, lobby
