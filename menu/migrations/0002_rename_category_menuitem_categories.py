# Generated by Django 4.2.7 on 2023-11-17 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menuitem", old_name="category", new_name="categories",
        ),
    ]
