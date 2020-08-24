from django.urls import path
from .views import Board

app_name = "game_board"
urlpatterns = [
    path("game/", Board.as_view(), name="game_board"),
]
