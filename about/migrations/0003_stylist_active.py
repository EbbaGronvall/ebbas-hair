# Generated by Django 4.2.14 on 2024-08-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_specialties_stylist_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylist',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
