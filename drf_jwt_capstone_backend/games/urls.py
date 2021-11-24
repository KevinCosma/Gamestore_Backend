from django.urls import path
from games import views

urlpatterns = [
    path('comments/videogames/', views.VideoGameCommentList.as_view()),
    path('comments/videogames/create/', views.VideoGameCommentList.as_view()),
    path('comments/cardgames/', views.CardGameCommentList.as_view()),
    path('comments/boardgames/', views.BoardGameCommentList.as_view()),
    path('comments/dndgames/', views.DnDCommentList.as_view()),
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>', views.GameDetail.as_view()),
    path('games/seller/<userid>/', views.GameDetail.as_view()),
    path('games/videogames/', views.VideoGameList.as_view()),
    path('games/cardgames/', views.CardGameList.as_view()),
    path('games/boardgames/', views.BoardGameList.as_view()),
    path('games/dnd/', views.DnDList.as_view()),
    path('shoppingcart/<userid>/', views.ShoppingCartDetail.as_view()),
    path('shoppingcart/<userid>/delete/<bookid>/', views.ShoppingCartDetail.as_view()),
    path('shoppingcart/update/<userid>/<bookid>/', views.ShoppingCartDetail.as_view()),
    path('shoppingcart/addGame/', views.ShoppingCartList.as_view()),
]