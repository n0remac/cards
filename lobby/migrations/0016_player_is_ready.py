# Generated by Django 3.1 on 2020-08-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0015_auto_20200820_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]