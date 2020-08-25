from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(default="")
    command = models.TextField(default="")

class Game(models.Model):
    player1 = models.IntegerField(default=0)
    player2 = models.IntegerField(default=0)
