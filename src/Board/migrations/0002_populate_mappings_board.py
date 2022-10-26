from django.db import migrations


def populate_mappings_and_board(apps, schema_editor):

    Property = apps.get_model("Stop", "Property")
    SpecialStop = apps.get_model("Stop", "SpecialStop")
    Mapping = apps.get_model("Board", "Mapping")
    Board = apps.get_model("Board", "Board")
    ContentType = apps.get_model("contenttypes", "ContentType")

    Properties = Property.objects.all()
    SpecialStops = SpecialStop.objects.all()

    MAPPINGS = [
        "Start",
        "Mumbai",
        "Water Works",
        "Railways",
        "Ahemdabad",
        "Income Tax",
        "Indore",
        "Chance",
        "Jaipur",
        "Jail",
        "Delhi",
        "Chandigarh",
        "Electricity",
        "Bus Company",
        "Shimla",
        "Amritsar",
        "Community Chest",
        "Srinagar",
        "Club",
        "Agra",
        "Chance",
        "Kanpur",
        "Patna",
        "Darjeeling",
        "Airways",
        "Kolkata",
        "Hyderabad",
        "Rest House",
        "Chennai",
        "Community Chest",
        "Bangalore",
        "Wealth Tax",
        "Mysore",
        "Pune",
        "Motor Boat",
        "Goa",
    ]

    mappings = []
    for index, mapping in enumerate(MAPPINGS):
        content_obj = Properties.filter(name=mapping)
        if not content_obj.exists():
            content_obj = SpecialStops.filter(name=mapping)

        mapping_obj = Mapping(
            content_type=ContentType.objects.get_for_model(content_obj[0]),
            object_id=content_obj[0].id,
            place_number=index + 1,
        )
        mapping_obj.full_clean()
        mappings.append(mapping_obj)

    mappings = Mapping.objects.bulk_create(mappings)

    board = Board()
    board.save()
    board.mappings.add(*list(mappings))


class Migration(migrations.Migration):

    dependencies = [("Board", "0001_initial"), ("Stop", "0002_populate_stops")]

    operations = [migrations.RunPython(populate_mappings_and_board)]
