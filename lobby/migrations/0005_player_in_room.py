# Generated by Django 3.1 on 2020-08-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0004_auto_20200817_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='in_room',
            field=models.BooleanField(default=False),
        ),
    ]
