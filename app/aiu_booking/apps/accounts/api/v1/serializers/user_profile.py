from rest_framework import serializers

from aiu_booking.apps.accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("email", "student_id")


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("student_id", )
