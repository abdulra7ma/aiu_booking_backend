from datetime import date

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from aiu_booking.apps.booking.models import Booking
from .facility import FacilitySerializer
from django.db.models import Q


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["facility", "title", "date", "start_time", "end_time"]

    def validate(self, attrs):
        if attrs["date"] < date.today():
            raise serializers.ValidationError(
                _("Booking date should not be on the past")
            )

        if attrs["end_time"] < attrs["start_time"]:
            raise serializers.ValidationError(
                _("Booking End time should be after start time")
            )

        if attrs["end_time"] == attrs["start_time"]:
            raise serializers.ValidationError(
                _("Booking end time should not be the same as start time")
            )

        bookings = Booking.objects.filter(
                Q(start_time__range=[attrs["start_time"], attrs["end_time"]])
                | Q(end_time__range=[attrs["start_time"], attrs["end_time"]])
        ).filter(Q(facility=attrs["facility"]))

        if bookings.exists():
            raise serializers.ValidationError(
                _("Can not book during that time, please check calender")
            )

        return attrs


class BookingSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer()

    class Meta:
        model = Booking
        fields = [
            "id",
            "facility",
            "date",
            "title",
            "start_time",
            "end_time",
            "created",
            "updated",
        ]
