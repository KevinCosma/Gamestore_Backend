from rest_framework import serializers
from .models import Game
from .models import Comment
from .models import Reply

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'user', 'title', 'description', 'price', 'ageRecommendation', 'category']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'text']


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = ['id', 'text', 'comment']