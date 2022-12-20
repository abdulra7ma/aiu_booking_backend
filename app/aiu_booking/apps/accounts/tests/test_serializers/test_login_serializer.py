from rest_framework.exceptions import ValidationError

import pytest

from aiu_booking.apps.accounts.api.v1.serializers.auth.signin import SignInSerializer


@pytest.mark.django_db
def test_login_serializer_validate_success(user_account):
    email = "jane@example.com"
    password = "super_secret_password"  # nosec
    user = user_account(email=email)
    user.set_password(password)
    user.save(update_fields=("password",))
    serializer = SignInSerializer()

    result = serializer.validate({"email": email, "password": password})
    assert result == {"user": user}


@pytest.mark.django_db
def test_login_serializer_validate_failure(user_account):
    email = "jane@example.com"
    password = "super_secret_password"  # nosec
    user = user_account(email=email)
    user.set_password(password)
    user.save(update_fields=("password",))
    serializer = SignInSerializer()

    with pytest.raises(ValidationError):
        serializer.validate({"email": email, "password": "incorrect"})
