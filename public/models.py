from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

class Trip(models.Model):
	driver = models.ForeignKey(User,
		on_delete=models.CASCADE,
		related_name='driver',
		verbose_name='Conducteur'
	)
	passengers = models.ManyToManyField(User,
		related_name='passengers',
		verbose_name='Passagers'
	)

	leaving_date = models.DateTimeField(verbose_name='Date de départ')
	origin = models.CharField(max_length=255, verbose_name='Origine')
	destination = models.CharField(max_length=255, verbose_name='Destination')
