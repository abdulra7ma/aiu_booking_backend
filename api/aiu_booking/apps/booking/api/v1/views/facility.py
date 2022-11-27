from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from drf_rw_serializers.generics import ListAPIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from aiu_booking.apps.booking.api.v1.serializers.facility import (
    FacilityCreateSerializer,
    FacilityImageSerializer,
    FacilitySerializer,
)
from aiu_booking.apps.booking.models.facility import Facility
from aiu_booking.apps.booking.utils.request import get_query_id
from aiu_booking.apps.booking.utils.swagger.facility import facility_id_param

from ._common import CoreCRUDAPIVIew


class CoreFacilityAPIVIew(CoreCRUDAPIVIew):
    def get_object(self):
        facility_id = get_query_id(self.request, _("Facility"))

        try:
            return Facility.objects.get(id=facility_id)
        except ObjectDoesNotExist:
            raise APIException(_("Facility not found"))


class FacilityAPIView(CoreFacilityAPIVIew):
    read_serializer_class = FacilitySerializer
    write_serializer_class = FacilityCreateSerializer

    @swagger_auto_schema(
        manual_parameters=[facility_id_param],
        tags=["facility"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Facility response object",
                schema=FacilitySerializer,
            )
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                "Facility response object",
                schema=FacilitySerializer,
            )
        },
        request_body=FacilityCreateSerializer,
        tags=["facility"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={status.HTTP_201_CREATED: openapi.Response("")},
        request_body=FacilityCreateSerializer,
        manual_parameters=[facility_id_param],
        tags=["facility"],
    )
    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, partial=True, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[facility_id_param], tags=["facility"]
    )
    def delete(self, request, *args, **kwargs):
        return super(FacilityAPIView, self).delete(request, *args, **kwargs)


class FacilityImageUploadAPIView(CoreFacilityAPIVIew):
    serializer_class = FacilityImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        manual_parameters=[facility_id_param],
        tags=["facility-image"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Facility Image response object",
                schema=FacilitySerializer,
            )
        },
    )
    def get(self, request, *args, **kwargs):
        return super(FacilityImageUploadAPIView, self).get(
            request, *args, **kwargs
        )

    @swagger_auto_schema(
        manual_parameters=[facility_id_param],
        tags=["facility-image"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Facility Image response object",
                schema=FacilitySerializer,
            )
        },
    )
    def post(self, request, *args, **kwargs):
        facility = self.get_object()
        serializer = self.get_serializer(instance=facility, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.add_image()
        return Response(
            FacilitySerializer(instance=facility).data,
            status=status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        manual_parameters=[facility_id_param],
        tags=["facility-image"],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Facility Image response object",
                schema=FacilitySerializer,
            )
        },
    )
    def patch(self, request, *args, **kwargs):
        facility = self.get_object()
        serializer = self.get_serializer(instance=facility, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update_image()
        return Response(
            FacilitySerializer(instance=facility).data,
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        manual_parameters=[facility_id_param], tags=["facility-image"]
    )
    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object())
        serializer.delete_image()
        return Response(status=status.HTTP_200_OK)


class FacilityListAPIView(ListAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
