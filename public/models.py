from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    #required by the auth model
    phone = models.CharField(max_length=12, null=True, blank=True)