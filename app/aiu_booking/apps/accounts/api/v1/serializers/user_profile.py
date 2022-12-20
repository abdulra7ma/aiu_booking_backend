from rest_framework import serializers

from aiu_booking.apps.accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("email", "student_id", "is_staff", "is_active", "date_joined", "is_superuser")


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("student_id", )
