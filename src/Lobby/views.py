from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from Lobby.models import Lobby
from Lobby.services import create_lobby


class LobbyList(APIView):
    """
    API to create or list a lobby
    """

    class LobbySerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50, required=False)
        password = serializers.CharField(max_length=50, required=False)

    def get(self, request, pk: int = None) -> Response:
        try:
            lobby = Lobby.objects.get(pk=pk)
        except Lobby.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.LobbySerializer(lobby)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = self.LobbySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        success, lobby = create_lobby(
            name=validated_data.get("name"), password=validated_data.get("password")
        )

        if not success:
            return Response(data=lobby, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.LobbySerializer(lobby)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        pass
