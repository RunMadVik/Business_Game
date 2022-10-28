from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(
        self, username, email, password=None, first_name=None, last_name=None
    ):
        if username is None:
            raise TypeError("User must have a username")

        if email is None:
            raise TypeError("User must have an email")

        if first_name and not last_name:
            raise TypeError("User must have a first name before a last name")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, username, email, password, first_name=None, last_name=None
    ):
        if password is None:
            raise TypeError("Superusers must have a password")

        user = self.create_user(username, email, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=128, unique=True)
    first_name = models.CharField(db_index=True, max_length=64, null=True, blank=True)
    last_name = models.CharField(db_index=True, max_length=64, null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        if not self.first_name:
            return None

        if not self.last_name:
            return self.first_name

        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=30)

        token = jwt.encode(
            {"id": self.pk, "exp": dt},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
