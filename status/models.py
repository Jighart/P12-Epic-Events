from django.db import models


class Status(models.Model):
    name = models.CharField(
        choices=[
            ('PENDING', 'PENDING'),
            ('SIGNED', 'SIGNED'),
            ('CREATED', 'CREATED'),
            ('CANCELLED', 'CANCELLED'),
            ('POSTPONED', 'POSTPONED'),
            ('COMPLETE', 'COMPLETE'),
        ],
        max_length=20,
        default='CREATED',
    )

    def __str__(self):
        return self.name
