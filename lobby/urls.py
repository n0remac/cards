from django.urls import path
from .views import Lobby, Room

app_name = "lobby"
urlpatterns = [
    path("", Lobby.as_view(), name="lobby"),
    path("room/", Room.as_view(), name="room"),
]
