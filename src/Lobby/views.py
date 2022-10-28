from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Lobby.models import Lobby
from Lobby.services import get_or_create_lobby
from Player.services.create import get_or_create_player


class LobbyList(APIView):
    """
    API to create or list a lobby
    """

    class LobbySerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50, required=False)
        password = serializers.CharField(max_length=50, required=False)
        starting_money = serializers.IntegerField(required=False)

    def get(self, request, pk: int = None) -> Response:
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            lobby = Lobby.objects.get(pk=pk, created_by=request.user)
        except Lobby.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.LobbySerializer(lobby)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        if not request.user.is_authenticated:
            return Response(
                {"Error": "Not an authenticated user"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.LobbySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        success, lobby = get_or_create_lobby(
            user=request.user,
            name=validated_data.get("name"),
            password=validated_data.get("password"),
            starting_money=validated_data.get("starting_money"),
        )

        if not success:
            return Response(data=lobby, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.LobbySerializer(lobby)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class LobbyPlayerList(APIView):
    """
    API to create a lobby player
    """

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        lobby_name = request.data.get("name")
        lobby_password = request.data.get("password")

        if not lobby_name or not lobby_password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            lobby = Lobby.objects.get(name=lobby_name, password=lobby_password)
        except Lobby.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        success, player = get_or_create_player(user=request.user, lobby=lobby)
        if not success:
            return Response({"Error": player}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
