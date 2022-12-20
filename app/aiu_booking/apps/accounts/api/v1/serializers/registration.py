from django.utils.translation import gettext

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from aiu_booking.apps.accounts.exceptions import InvalidPasswordError
from aiu_booking.apps.accounts.models import UserAccount
from aiu_booking.apps.accounts.services.password import PasswordService


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, max_length=128)
    student_id = serializers.CharField(write_only=True, max_length=128)
    password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = UserAccount
        fields = ("email", "student_id", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password_service = PasswordService()

    def validate_email(self, email):
        if UserAccount.objects.filter(email=email).exists():
            raise ValidationError(
                gettext("Could not create account with this email.")
            )

        if UserAccount.objects.filter(student_id=email).exists():
            raise ValidationError(
                gettext("could not create account with this student id.")
            )

        return super().validate(email)

    def validate_student_id(self, student_id):
        if UserAccount.objects.filter(student_id=student_id).exists():
            raise ValidationError(
                gettext("could not create account with this student id.")
            )

        return super().validate(student_id)


    def validate_password(self, new_password):
        try:
            self.password_service.validate_password(new_password)
        except InvalidPasswordError as e:
            raise serializers.ValidationError(e.messages) from e
        return new_password

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        raw_password = self.validated_data.get("password")
        self.instance.set_password(raw_password)
        self.instance.save()
        return self.instance
