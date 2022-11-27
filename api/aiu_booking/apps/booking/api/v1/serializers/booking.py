from rest_framework import serializers

from aiu_booking.apps.booking.models import Booking

from .facility import FacilitySerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        field = ["facility", "date", "start_time", "end_time"]


class BookingSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer()

    class Meta:
        model = Booking
        field = ["id", "facility", "date", "start_time", "end_time"]
