from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User objects have the following fields:
        username
        first_name - Optional (blank=True)
        last_name - Optional (blank=True)
        email - Optional (blank=True)
        password
        groups
        user_permissions
        is_staff
        is_active
        is_superuser
        last_login
        date_joined
        """
    sms_telephone = models.CharField(verbose_name='telephone', max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.CharField(max_length=5, null=True, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
