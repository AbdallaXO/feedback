# Generated by Django 5.1.4 on 2025-01-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_remove_userprofile_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
