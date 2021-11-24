from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
User = get_user_model()

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    ageRecommendation = models.IntegerField(null=True)
    category = models.CharField(max_length=150)



class Comment(models.Model):
    topic = models.CharField(max_length=20, null=True)
    text = models.CharField(max_length=500)

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Users(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    
class Role(models.Model):
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=True)

