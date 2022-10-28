import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from Users.models import User


def get_user(auth_token: str):
    try:
        data = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise Exception("Token Signature has expired")
    except jwt.InvalidSignatureError:
        raise Exception("Token Signature is invalid")

    try:
        user = User.objects.get(pk=data["id"])
    except User.DoesNotExist:
        raise Exception("Given auth token is not valid")

    return user


class CustomAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        breakpoint()
        auth_token = request.headers.get("Authorization")
        if auth_token:
            auth, token = auth_token.split(" ")
            request.user = get_user(token)
