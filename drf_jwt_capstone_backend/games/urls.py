from django.urls import path
from games import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('comments/reply/', views.ReplyDetail.as_view()),
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>', views.GameDetail.as_view())
]