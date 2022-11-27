from django.db import models
from aiu_booking.apps.common.models.core import CoreModel
from django.utils.translation import gettext_lazy as _
from .facility import Facility
from datetime import date as python_date


class Booking(CoreModel):
    facility = models.ForeignKey(Facility, verbose_name=_("Booked Facility"), on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name=_("Booking date"), default=python_date.today())
    start_time = models.TimeField(verbose_name=_("Start time date"))
    end_time = models.TimeField(verbose_name=_("End time date"))

