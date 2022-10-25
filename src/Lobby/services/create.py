from typing import Optional, Tuple, Union

from django.core.exceptions import ValidationError

from Lobby.helpers import generate_random_string
from Lobby.models import Lobby


def create_lobby(
    name: Optional[str], password: Optional[str]
) -> Tuple[bool, Union[Lobby, str]]:
    name = name or generate_random_string(length=10)
    password = password or generate_random_string(length=10)

    lobby = Lobby(name=name, password=password)
    try:
        lobby.save()
    except ValidationError as error:
        return False, str(error)

    return True, lobby
