from django.urls import path

from Lobby.views import LobbyList

urlpatterns = [
    path("create/", LobbyList.as_view(), name="create-lobby"),
    path("<slug:pk>/", LobbyList.as_view(), name="get-lobby"),
]
