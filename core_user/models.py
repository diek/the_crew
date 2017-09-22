from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_ignition_locking_auth = models.BooleanField(default=False)
    license_issue_date = models.DateField(null=True, blank=True)
    license_expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = (("Can view driver info", "view_driver_info"),)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Driver.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
