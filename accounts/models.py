from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    tel = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)