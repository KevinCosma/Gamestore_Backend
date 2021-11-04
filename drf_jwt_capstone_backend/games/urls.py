from django.urls import path
from games import views

urlpatterns = [
    path('all/', views.get_all_games)
]