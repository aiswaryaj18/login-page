from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields and configurations here
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)

    # Add any other custom configurations or methods here
