from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

class Trip(models.Model):
	driver = models.ForeignKey(User,
		on_delete=models.CASCADE,
		related_name='driver'
	)
	passengers = models.ManyToManyField(User,
		related_name='passengers'
	)

	departure_date = models.DateTimeField()
	origin = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
