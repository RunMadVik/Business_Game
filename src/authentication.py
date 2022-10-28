from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = request._request.user
        if not user.is_authenticated:
            raise AuthenticationFailed("Not an authenticated user")

        if not user.is_active:
            raise AuthenticationFailed("User inactive or deleted")

        return (user, None)
