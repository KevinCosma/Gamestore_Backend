from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videoGame = models.CharField(max_length=50)
    cardGame = models.CharField(max_length=50)
    boardGame = models.CharField(max_length=50)