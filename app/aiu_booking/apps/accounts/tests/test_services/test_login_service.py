from django.test.client import RequestFactory
from django.urls import reverse

from rest_framework import status

import pytest

from aiu_booking.apps.accounts.services.signin import SignInService


@pytest.mark.django_db
def test_login_service_login(user_account, mocker):
    request = mocker.MagicMock()
    user = user_account()
    service = SignInService
    mocked_django_login = mocker.patch.object(service, "_django_login")

    response = service.login(request, user)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    mocked_django_login.assert_called_once_with(request, user)


def test_login_service_logout(user_account, mocker):
    user = user_account()
    request = RequestFactory().post(reverse("app-v1-accounts:logout"))
    request.user = user
    service = SignInService
    mocked_django_logout = mocker.patch.object(service, "_django_logout")

    response = service.logout(request)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    mocked_django_logout.assert_called_once_with(request)
