from uuid import uuid4

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Mapping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    place_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(36)]
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    mappings = models.ManyToManyField(Mapping)

    def __str__(self) -> str:
        return str(self.id)
