# Generated by Django 4.2.14 on 2024-08-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
