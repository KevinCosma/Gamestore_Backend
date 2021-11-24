from rest_framework import serializers
from .models import Game, ShoppingCart, User, Role
from .models import Comment

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'price', 'ageRecommendation', 'category']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'text']


class ShoppingCartSerializer(serializers.Serializer):

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'game', 'quantity']

class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'username']

class Role(serializers.Serializer):

    class Meta:
        model = Role
        fields = ['id', 'seller', 'buyer']