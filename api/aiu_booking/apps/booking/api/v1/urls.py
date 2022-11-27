from django.urls import path

from aiu_booking.apps.booking.api.v1.views.facility import FacilityAPIView


urlpatterns = [path("", FacilityAPIView.as_view(), name="facility")]
