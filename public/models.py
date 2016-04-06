from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended user model. Stores additional fields needed for TravelExpress"""

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile'
                                )

    phone = models.CharField(max_length=10, default='')
    tolerates = models.CharField(max_length=500, default='', blank=True)
    does_not_tolerate = models.CharField(max_length=500, default='', blank=True)


class Trip(models.Model):
    """A Trip represents a single A-to-B trip with one driver and multiple passengers"""

    driver = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='driver'
                               )
    passengers = models.ManyToManyField(User,
                                        related_name='passengers'
                                        )

    departure_date = models.DateTimeField()
    origin = models.CharField(max_length=255, default='')
    destination = models.CharField(max_length=255, default='')
    is_canceled = models.BooleanField(default=False)
