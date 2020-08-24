from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20)
    needs_match = models.BooleanField(default=True)
    opponent = models.IntegerField(default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "needs_match": self.needs_match,
            "opponent": self.opponent,
        }
