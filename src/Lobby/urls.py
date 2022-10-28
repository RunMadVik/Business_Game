from django.urls import path

from Lobby.views import CreateLobby, GetLobby

urlpatterns = [
    path("create/", CreateLobby.as_view(), name="create-lobby"),
    path("<uuid:pk>/", GetLobby.as_view(), name="get-lobby"),
]
