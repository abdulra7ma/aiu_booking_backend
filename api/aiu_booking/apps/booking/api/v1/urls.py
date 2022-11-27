from django.urls import path

from aiu_booking.apps.booking.api.v1.views.facility import (
    FacilityAPIView,
    FacilityImageUploadAPIView,
    FacilityListAPIView,
)


urlpatterns = [
    path("", FacilityAPIView.as_view(), name="facility"),
    path(
        "/image", FacilityImageUploadAPIView.as_view(), name="facility-image"
    ),
    path("/all", FacilityListAPIView.as_view(), name="facility-all"),
]
