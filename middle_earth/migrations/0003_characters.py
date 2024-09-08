# Generated by Django 5.0.6 on 2024-09-08 01:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("middle_earth", "0002_alter_verses_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Characters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "race",
                    models.CharField(
                        choices=[
                            ("Human", "Human"),
                            ("Elf", "Elf"),
                            ("Dwarf", "Dwarf"),
                            ("Valar", "Valar"),
                            ("Maiar", "Maiar"),
                            ("Orc", "Orc"),
                            ("Uruk-Hai", "Uruk-Hai"),
                            ("Goblin", "Goblin"),
                            ("Eagle", "Eagle"),
                            ("Spider", "Spider"),
                            ("Troll", "Troll"),
                            ("Ent", "Ent"),
                            ("Balrog", "Balrog"),
                            ("Dragon", "Dragon"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
    ]
