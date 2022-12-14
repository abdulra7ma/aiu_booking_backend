from django.urls import path

from aiu_booking.apps.accounts.api.v1.views.signin import SignInAPIView, LogoutView
from aiu_booking.apps.accounts.api.v1.views.password import (
    ChangePasswordAPIView,
    ConfirmResetPasswordAPIView,
    ResetPasswordAPIView,
)
from aiu_booking.apps.accounts.api.v1.views.signup import (
    SignUpAPIView,
)
from aiu_booking.apps.accounts.api.v1.views.user_profile import (
    UserProfileAPIView,
)


urlpatterns = [
    path("signin/", SignInAPIView.as_view(), name="signin"),
    path("signout/", LogoutView.as_view(), name="signout"),
    path("me/", UserProfileAPIView.as_view(), name="user-profile"),
    path("password/", ChangePasswordAPIView.as_view(), name="change-password"),
    path(
        "password/confirm/",
        ConfirmResetPasswordAPIView.as_view(),
        name="confirm-reset-password",
    ),
    path(
        "password/reset/",
        ResetPasswordAPIView.as_view(),
        name="reset-password",
    ),
    path("signup/", SignUpAPIView.as_view(), name="signup"),
]
