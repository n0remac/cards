# Generated by Django 3.1 on 2020-08-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0010_auto_20200820_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='opponent',
            field=models.IntegerField(default=None),
        ),
    ]
