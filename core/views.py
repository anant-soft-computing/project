# class Perform
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Registration
from .serializers import RegistrationSerializer, EventRegistrationSerializer


class UserEvents(APIView):
    """
    The UserEvents class is an API view
    that retrieves the events registered by a user with a given ID."""

    def get(self, request, id, format=None):
        try:
            user = Registration.objects.get(id=id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RegistrationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConfirmPresentView(APIView):
    """
    The `ConfirmPresentView` class is an API view that allows a user to confirm their presence at an
    event they are registered for."""

    def get(self, request, user_id, event_id, format=None):
        try:
            user = Registration.objects.get(id=user_id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user.events.filter(event__id=event_id).exists():
            EventRegistration_instance = user.events.get(event__id=event_id)
            event_data = EventRegistration_instance.event

            if event_data.event_start_date > timezone.localtime().date():
                return Response(
                    "The event has not started yet",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif event_data.event_end_date < timezone.localtime().date():
                return Response(
                    "The event has already ended",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            elif (
                (event_data.event_start_date == timezone.localtime().date())
                and (timezone.localtime().time() >= event_data.event_start_time)
                and (timezone.localtime().time() < event_data.event_end_time)
            ):
                if (
                    not EventRegistration_instance.present
                    and not EventRegistration_instance.can_attend_multiple
                ):
                    EventRegistration_instance.present = True
                    EventRegistration_instance.attend_event_count += 1
                    EventRegistration_instance.save()

                    return Response(status=status.HTTP_200_OK)

                elif (
                    EventRegistration_instance.present
                    and not EventRegistration_instance.can_attend_multiple
                ):
                    return Response(
                        "You already have attended this event",
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                elif EventRegistration_instance.can_attend_multiple:
                    EventRegistration_instance.present = True
                    EventRegistration_instance.attend_event_count += 1
                    EventRegistration_instance.save()

                    return Response(status=status.HTTP_200_OK)

        else:
            return Response(
                "You are not registered for this event.",
                status=status.HTTP_404_NOT_FOUND,
            )


class ConfirmAuditoriumAndREGView(APIView):
    def get(self, request, user_id, event_id, format=None):
        try:
            user = Registration.objects.get(id=user_id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user.events.filter(event__id=event_id).exists():
            EventRegistration_instance = user.events.get(event__id=event_id)

            EventRegistration_instance.present = True
            EventRegistration_instance.attend_event_count += 1
            EventRegistration_instance.save()

            return Response(status=status.HTTP_200_OK)

        else:
            return Response(
                "You are not registered for this event.",
                status=status.HTTP_404_NOT_FOUND,
            )

class UpdateRegistrationView(APIView):
    def post(self, request, id, format=None):
        try:
            registration = Registration.objects.get(id=id)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RegistrationSerializer(registration, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
            