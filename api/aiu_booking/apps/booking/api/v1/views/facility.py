from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from aiu_booking.apps.booking.api.v1.serializers.facility import (
    FacilityCreateSerializer,
    FacilitySerializer,
)
from aiu_booking.apps.booking.models.facility import Facility
from aiu_booking.apps.booking.utils.request import get_query_id


class FacilityAPIView(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    def get_object(self):
        facility_id = get_query_id(self.request, _("Facility"))

        try:
            return Facility.objects.get(id=facility_id)
        except ObjectDoesNotExist:
            raise APIException(_("Facility not found"))

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, partial=True, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return FacilityCreateSerializer
        return FacilitySerializer
