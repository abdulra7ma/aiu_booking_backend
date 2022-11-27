from rest_framework import serializers

from aiu_booking.apps.booking.models import Facility


class FacilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["name", "bio"]


class FacilityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["image"]

    def add_image(self):
        self.instance.image = self.validated_data["image"]
        self.instance.save()
        return self.instance

    def update_image(self):
        self.instance.image = self.validated_data["image"]
        self.instance.save()
        return self.instance

    def delete_image(self):
        self.instance.image = ""
        self.instance.save()
        return self.instance



class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "name", "bio", "image"]
