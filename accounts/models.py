from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    EMAIL_FIELD = 'email'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255, unique=True)

    def __str__(self):
        return self.username
