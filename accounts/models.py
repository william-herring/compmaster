from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager


class User(AbstractUser):
    wca_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    is_delegate = models.BooleanField(default=False)
    profile_picture = models.CharField(max_length=500)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "wca_id"
