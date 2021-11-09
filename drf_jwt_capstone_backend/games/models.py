from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
User = get_user_model()

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    ageRecommendation = models.IntegerField(null=True)
    category = models.CharField(max_length=150)

class Comment(models.Model):
    text = models.CharField(max_length=500)

class Reply(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    text = models.CharField(max_length=500) 