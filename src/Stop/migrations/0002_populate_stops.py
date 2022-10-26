from django.db import migrations


def populate_stops(apps, schema_editor):
    """
    This is a function to populate all the existing models in the application
    """

    Property = apps.get_model("Stop", "Property")
    Place = apps.get_model("Stop", "Place")
    SpecialStop = apps.get_model("Stop", "SpecialStop")

    PROPERTIES = (
        ("Mumbai", 1, 1200, 8500, 4250, False),
        ("Ahemdabad", 1, 400, 4000, 2000, False),
        ("Darjeeling", 1, 200, 2500, 1250, False),
        ("Kolkata", 1, 800, 6500, 3250, False),
        ("Hyderabad", 1, 300, 3500, 1750, False),
        ("Indore", 1, 200, 1500, 750, False),
        ("Jaipur", 1, 250, 3000, 1500, False),
        ("Agra", 1, 200, 2500, 1250, False),
        ("Kanpur", 1, 400, 4000, 2000, False),
        ("Patna", 1, 150, 2000, 1000, False),
        ("Shimla", 1, 200, 2200, 1100, False),
        ("Amritsar", 1, 300, 3300, 1650, False),
        ("Srinagar", 1, 550, 5000, 2500, False),
        ("Chennai", 1, 900, 7000, 3500, False),
        ("Bangalore", 1, 400, 4000, 2000, False),
        ("Delhi", 1, 750, 6000, 3000, False),
        ("Chandigarh", 1, 200, 2500, 1250, False),
        ("Mysore", 1, 200, 2500, 1250, False),
        ("Pune", 1, 300, 3000, 1500, False),
        ("Goa", 1, 400, 4000, 2000, False),
        ("Bus Company", 2, 600, 3500, 1750, False),
        ("Airways", 2, 3000, 10500, 5250, False),
        ("Electricity", 2, 2500, 2500, 1250, False),
        ("Water Works", 2, 500, 3200, 1600, False),
        ("Motor Boat", 2, 2500, 5500, 1750, False),
        ("Railways", 2, 1000, 9500, 4750, False),
    )

    PLACES = (
        ("RED", 4000, 5500, 7000, 9000, 7500, 7500),
        ("RED", 1500, 3000, 4200, 5000, 4500, 4500),
        ("RED", 1200, 2600, 3500, 5000, 3000, 3000),
        ("RED", 3200, 4500, 6500, 8000, 6000, 6000),
        ("RED", 1200, 3000, 4500, 6000, 5000, 5000),
        ("BLUE", 6000, 1500, 2500, 3600, 2000, 2000),
        ("BLUE", 1500, 2750, 4000, 5500, 4000, 4000),
        ("BLUE", 900, 1600, 2500, 3500, 3000, 3000),
        ("BLUE", 1500, 3000, 4500, 5500, 4500, 4500),
        ("BLUE", 800, 2000, 3000, 4500, 2500, 2500),
        ("YELLOW", 1000, 2750, 4500, 6000, 3500, 3500),
        ("YELLOW", 1400, 2800, 4000, 5000, 4500, 4500),
        ("YELLOW", 3500, 5000, 7000, 8000, 6000, 6000),
        ("YELLOW", 3500, 5000, 7000, 8500, 6500, 6500),
        ("YELLOW", 1500, 3000, 4500, 5500, 4500, 4500),
        ("GREEN", 3000, 4300, 5500, 7500, 5000, 5000),
        ("GREEN", 900, 1600, 2500, 3500, 3000, 3000),
        ("GREEN", 1000, 2500, 3500, 4500, 3000, 3000),
        ("GREEN", 1200, 2000, 4500, 5500, 4000, 4000),
        ("GREEN", 2200, 3500, 5000, 6500, 4500, 4500),
    )

    SPECIAL_STOPS = [
        "Start",
        "Income Tax",
        "Chance",
        "Jail",
        "Community Chest",
        "Club",
        "Rest House",
        "Wealth Tax",
    ]

    special_stops = []
    for special_stop in SPECIAL_STOPS:
        special_obj = SpecialStop(name=special_stop)
        special_obj.full_clean()
        special_stops.append(special_obj)

    special_stops = SpecialStop.objects.bulk_create(special_stops)

    properties = []
    for property in PROPERTIES:
        property_obj = Property(
            name=property[0],
            property_type=property[1],
            rent=property[2],
            cost_of_acquisition=property[3],
            bank_mortgage_value=property[4],
            mortgaged=property[5],
        )
        property_obj.full_clean()
        properties.append(property_obj)

    properties = Property.objects.bulk_create(properties)

    places = []
    for index, place in enumerate(PLACES):
        place_obj = Place(
            property=properties[index],
            property_color=place[0],
            rent_with_one_house=place[1],
            rent_with_two_house=place[2],
            rent_with_three_house=place[3],
            rent_with_hotel=place[4],
            cost_of_house=place[5],
            cost_of_hotel=place[6],
        )
        place_obj.full_clean()
        places.append(place_obj)

    places = Place.objects.bulk_create(places)


class Migration(migrations.Migration):

    dependencies = [("Stop", "0001_initial")]

    operations = [migrations.RunPython(populate_stops)]
