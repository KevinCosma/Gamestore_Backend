from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http.response import Http404
from .models import Game
from .models import Comment
from .serializers import GameSerializer, ShoppingCartSerilaizer
from .serializers import CommentSerializer
from .serializers import ShoppingCart
from django.contrib.auth import get_user_model
User = get_user_model()

class VideoGameCommentList(APIView):

    def get(self, request):
        comment = Comment.objects.filter(topic='Video Games')
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.topic = 'Video Games'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardGameCommentList(APIView):

    def get(self,request):
        comment = Comment.objects.filter(topic='Card Games')
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.topic = 'Card Games'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardGameCommentList(APIView):

    def get(self,request):
        comment = Comment.objects.filter(topic='Board Games')
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.topic = 'Board Games'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DnDCommentList(APIView):   

    def get(self,request):
        comment = Comment.objects.filter(topic='DnD')
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.topic = 'DnD'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameList(APIView):

    def get(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetail(APIView):

    def get_object(self,pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def delete(self, request, pk):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VideoGameList(APIView):

    def get(self,request):
        videogame = Game.objects.filter(category = "Video Game")
        serializer = GameSerializer(videogame, many=True)
        return Response(serializer.data)

class CardGameList(APIView):

    def get(self,request):
        cardgame = Game.objects.filter(category = "Card Game")
        serializer = GameSerializer(cardgame, many=True)
        return Response(serializer.data)

class BoardGameList(APIView):

    def get(self,request):
        boardgame = Game.objects.filter(category = "Board Game")
        serializer = GameSerializer(boardgame, many=True)
        return Response(serializer.data)

class DnDList(APIView):

    def get(self,request):
        dnd = Game.objects.filter(category = "DnD")
        serializer = GameSerializer(dnd, many=True)
        return Response(serializer.data)

class ShoppingCart(APIView):
    
    def get(self,request):
        shoppingCart = ShoppingCart.all()
        serializer = ShoppingCartSerilaizer(shoppingCart, many=True)
        return Response(serializer.data)