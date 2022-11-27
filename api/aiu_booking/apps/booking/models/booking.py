from datetime import date as python_date

from django.db import models
from django.utils.translation import gettext_lazy as _

from aiu_booking.apps.common.models.core import CoreModel

from .facility import Facility
from django.utils import timezone


class Booking(CoreModel):
    facility = models.ForeignKey(
        Facility,
        verbose_name=_("Booked Facility"),
        on_delete=models.SET_NULL,
        null=True,
    )
    date = models.DateField(
        verbose_name=_("Booking date"), default=timezone.now()
    )
    start_time = models.TimeField(verbose_name=_("Start time date"))
    end_time = models.TimeField(verbose_name=_("End time date"))
