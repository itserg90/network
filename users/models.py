from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Email address"
    )
    phone = models.CharField(
        max_length=35, verbose_name="phone", help_text="Enter phone number", **NULLABLE
    )

    city = models.CharField(
        max_length=100, verbose_name="city", help_text="Enter city", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
