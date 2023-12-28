# class Perform
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Registration
from .serializers import EventSerializer


class UserEvents(APIView):
    def get(self, request, id, format=None):
        try:
            user = Registration.objects.get(id=id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(user.events.all(), many=True)
        return Response(serializer.data)
