from rest_framework import serializers
from .models import Game, GameType

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','user', 'videoGame', 'cardGame', 'boardGame']
    
    class Meta:
        model = GameType
        fields = ['id', 'type', 'price']