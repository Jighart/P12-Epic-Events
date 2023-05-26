from django.conf import settings
from django.db import models

from clients.models import Client
from users.models import SALES
from status.models import Status


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'team': SALES}
    )
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        limit_choices_to={"status": True},
        related_name="contract",
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_NULL,
        null=True,
        default=1,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    payment_due = models.DateField()

    def __str__(self):
        return f"Contract {self.id}"
