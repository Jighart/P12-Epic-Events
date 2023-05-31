from django.db import models

STATUS = [
            ('PENDING', 'PENDING'),
            ('SIGNED', 'SIGNED'),
            ('CREATED', 'CREATED'),
            ('CANCELLED', 'CANCELLED'),
            ('POSTPONED', 'POSTPONED'),
            ('COMPLETE', 'COMPLETE'),
        ]


class Status(models.Model):
    name = models.CharField(
        choices=STATUS,
        max_length=20,
        default='CREATED',
    )

    def __str__(self):
        return self.name
