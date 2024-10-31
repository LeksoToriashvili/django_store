from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserModel(AbstractUser):
    last_active_datetime = models.DateTimeField(blank=True, null=True)
