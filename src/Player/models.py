from uuid import uuid4

from django.db import models

from Stop.models import Property


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    properties = models.ManyToManyField(Property)
