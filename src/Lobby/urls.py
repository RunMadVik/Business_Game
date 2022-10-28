from django.urls import path

from Lobby.views import CreateLobby, CreateLobbyPlayer, GetLobby

urlpatterns = [
    path("create/", CreateLobby.as_view(), name="create-lobby"),
    path("<uuid:pk>/", GetLobby.as_view(), name="get-lobby"),
    path("join/", CreateLobbyPlayer.as_view(), name="join-lobby"),
]
