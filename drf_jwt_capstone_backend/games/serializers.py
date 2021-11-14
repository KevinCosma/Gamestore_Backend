from rest_framework import serializers
from .models import Game, ShoppingCart, Users
from .models import Comment

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'user', 'title', 'description', 'price', 'ageRecommendation', 'category']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'user', 'text']


class ShoppingCartSerilaizer(serializers.Serializer):

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'game']

class UsersSerializer(serializers.Serializer):

    class Meta:
        model = Users
        fields = ['id', 'firstName', 'lastName', 'email', 'username', 'street', 'city', 'state', 'zipCode']

class Roles(serializers.Serializer):

    class Meta:
        fields = ['id', 'seller', 'buyer']