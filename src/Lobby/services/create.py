from typing import Optional, Tuple, Union

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from Lobby.helpers import generate_random_string
from Lobby.models import Lobby, LobbyPlayer
from Player.models import Player
from Player.services import create_player


def create_lobby(
    user: User,
    name: Optional[str],
    password: Optional[str],
    starting_money: Optional[int],
) -> Tuple[bool, Union[Lobby, str]]:

    lobby = Lobby(
        name=name or generate_random_string(length=10),
        password=password or generate_random_string(length=10),
        created_by=user,
    )
    try:
        lobby.save()
    except ValidationError as error:
        return False, str(error)

    success, player = create_player(user=user, money=starting_money or 30000)
    if not success:
        return success, player

    success, lobby_player = create_lobby_player(lobby=lobby, player=player)
    if not success:
        return success, lobby_player

    return True, lobby


def create_lobby_player(
    lobby: Lobby, player: Player
) -> Tuple[bool, Union[str, LobbyPlayer]]:
    lobby_player = LobbyPlayer(lobby=lobby, player=player)
    try:
        lobby_player.save()
    except ValidationError as error:
        return False, str(error)

    return True, lobby_player
