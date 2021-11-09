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
from .models import Reply
from .serializers import GameSerializer
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404    
   
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyDetail(APIView):

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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