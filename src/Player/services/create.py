from typing import Optional, Tuple, Union

from django.core.exceptions import ValidationError

from Player.models import Player
from Users.models import User


def create_player(
    user: User, money: int, name=Optional[str]
) -> Tuple[bool, Union[str, Player]]:
    player = Player(user=user, money=money, name=name or user.get_short_name())
    try:
        player.save()
    except ValidationError as error:
        return False, str(error)

    return True, player
