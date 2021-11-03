from django.urls import path
from gamestore import views

urlpatters = [
    path('', views.GameList.as_view())
]