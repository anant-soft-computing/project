# class Perform
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Registration
from .serializers import EventRegistrationSerializer


class UserEvents(APIView):
    def get(self, request, id, format=None):
        try:
            user = Registration.objects.get(id=id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventRegistrationSerializer(user.events.all(), many=True)
        return Response(serializer.data)


class ConfirmPresentView(APIView):
    def get(self, request, user_id, event_id, format=None):
        try:
            user = Registration.objects.get(id=user_id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user.events.filter(id=event_id).exists():
            event = user.events.get(id=event_id)
            event_data = event.event

            if event_data.event_start_date > timezone.now().date():
                return Response(
                    "The event has not started yet",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif event_data.event_end_date < timezone.now().date():
                return Response(
                    "The event has already ended",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if not event.present and not event.can_attend_multiple:
                event.present = True
                event.save()

            elif event.present and not event.can_attend_multiple:
                return Response(
                    "You already have attended this event",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif event.can_attend_multiple:
                event.present = True
                event.save()

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(
                "You are not registered for this event.",
                status=status.HTTP_404_NOT_FOUND,
            )
