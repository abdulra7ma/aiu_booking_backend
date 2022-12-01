from rest_framework import serializers

from aiu_booking.apps.booking.models import Booking
from django.utils.translation import gettext_lazy as _
from .facility import FacilitySerializer

from datetime import date


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["facility", "date", "start_time", "end_time"]

    def validate(self, attrs):
        if attrs["date"] < date.today():
            raise serializers.ValidationError(_("Booking date should be specified on the past"))

        if attrs["end_time"] < attrs["start_time"]:
            raise serializers.ValidationError(_("Booking End time should be after start time"))

        if attrs["end_time"] == attrs["start_time"]:
            raise serializers.ValidationError(_("Booking end time should not be the same as start time"))

        return attrs


class BookingSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer()

    class Meta:
        model = Booking
        fields = ["id", "facility", "date", "start_time", "end_time", "created", "updated"]
