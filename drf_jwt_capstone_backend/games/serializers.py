from rest_framework import serializers
from .models import Game
from .models import Comment

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'user', 'title', 'description', 'price', 'ageRecommendation', 'category']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'user', 'text']


# class DiscussionPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DiscussionPost
#         fields = ['id', 'comment', 'reply']