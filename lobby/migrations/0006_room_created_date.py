# Generated by Django 3.1 on 2020-08-19 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0005_player_in_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
