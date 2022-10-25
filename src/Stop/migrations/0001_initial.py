# Generated by Django 4.1.2 on 2022-10-17 12:04

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                (
                    "property_type",
                    models.IntegerField(
                        choices=[(1, "Place"), (2, "Utility")], default=1
                    ),
                ),
                ("rent", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "cost_of_acquisition",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "bank_mortgage_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("mortgaged", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="SpecialStop",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "rent_with_one_house",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "rent_with_two_house",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "rent_with_three_house",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "rent_with_hotel",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "property",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Stop.property"
                    ),
                ),
            ],
        ),
    ]