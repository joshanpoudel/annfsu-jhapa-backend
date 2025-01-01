from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from core.response import CustomResponse
from team.models import OurTeam
from team.serializer import TeamSerializer


class OurTeamView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        our_team = OurTeam.objects.first()

        if our_team is None:
            return CustomResponse.error(message="Team doesn't exist yet!")
        serializer = TeamSerializer(instance=our_team)

        return CustomResponse.success(
            data=serializer.data, message="Team fetched successfully!"
        )
