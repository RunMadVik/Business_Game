from uuid import uuid4

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from Board.models import Mapping


class Property(models.Model):
    class PropertyType(models.IntegerChoices):
        PLACE = 1
        UTILITY = 2

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30)
    property_type = models.IntegerField(
        choices=PropertyType.choices, default=PropertyType.PLACE
    )
    rent = models.DecimalField(max_digits=5, decimal_places=2)
    cost_of_acquisition = models.DecimalField(max_digits=10, decimal_places=2)
    bank_mortgage_value = models.DecimalField(max_digits=10, decimal_places=2)
    mortgaged = models.BooleanField(default=False)
    mapped_to = GenericRelation(Mapping)

    class Meta:
        verbose_name_plural = "Properties"


class Place(models.Model):

    COLOR_CHOICES = (
        ("RED", "RED"),
        ("BLUE", "BLUE"),
        ("YELLOW", "YELLOW"),
        ("GREEN", "GREEN"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    property_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    rent_with_one_house = models.DecimalField(max_digits=5, decimal_places=2)
    rent_with_two_house = models.DecimalField(max_digits=5, decimal_places=2)
    rent_with_three_house = models.DecimalField(max_digits=5, decimal_places=2)
    rent_with_hotel = models.DecimalField(max_digits=5, decimal_places=2)


class SpecialStop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30)
