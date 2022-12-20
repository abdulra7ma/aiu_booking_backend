from datetime import date as python_date

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from aiu_booking.apps.common.models.core import CoreModel

from .facility import Facility


class Booking(CoreModel):
    facility = models.ForeignKey(
        Facility,
        verbose_name=_("Booked Facility"),
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(verbose_name=_("Booking Title"), max_length=1048, null=True, blank=True)
    date = models.DateField(
        verbose_name=_("Booking date"), default=timezone.now()
    )
    start_time = models.TimeField(verbose_name=_("Start time date"))
    end_time = models.TimeField(verbose_name=_("End time date"))

    def __str__(self):
        if self.facility:
            return str(self.facility.pk) + " -> " + self.title
        return self.title
