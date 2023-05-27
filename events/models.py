from django.conf import settings
from django.db import models

from contracts.models import Contract
from users.models import SUPPORT
from status.models import Status


class Event(models.Model):
    contract = models.ForeignKey(
        to=Contract,
        on_delete=models.CASCADE,
        limit_choices_to={'status': True},
        related_name='event'
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'team': SUPPORT},
    )
    event_status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_NULL,
        null=True,
        default=3,
    )
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
