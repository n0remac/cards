from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(default="")
    command = models.TextField(default="")


class Game(models.Model):
    player1 = models.IntegerField(default=0)
    player2 = models.IntegerField(default=0)
    whos_turn = models.IntegerField(default=0)
    player1Cards = models.JSONField(default=str)
    player2Cards = models.JSONField(default=str)
