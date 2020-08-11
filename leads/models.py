from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    command = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)