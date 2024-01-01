from rest_framework import serializers

from .models import Event, EventRegistration, Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = "__all__"

    def get_events(self, obj):
        return obj.events.all().values("event__event_name", "event__id")


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = (
            "id",
            "event",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["event"] = instance.event.event_name
        return data
