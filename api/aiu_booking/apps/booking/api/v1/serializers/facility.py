from rest_framework import serializers

from aiu_booking.apps.booking.models import Facility


class FacilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["name", "bio"]


class FacilityImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["image"]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name", "bio", "image"]
