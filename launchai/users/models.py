from django.db import models

from django.contrib.auth.models import AbstractUser



AUTH_PROVIDERS = {
    'google': 'google',
    'email': 'email'
}

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    auth_provider = models.CharField(
        max_length=255, default=AUTH_PROVIDERS.get('email')
    )
    
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    