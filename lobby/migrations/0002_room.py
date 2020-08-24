# Generated by Django 3.1 on 2020-08-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.TextField(default=0)),
                ('player2', models.TextField(default=0)),
                ('ready1', models.BooleanField(default=False)),
                ('ready2', models.BooleanField(default=False)),
            ],
        ),
    ]
