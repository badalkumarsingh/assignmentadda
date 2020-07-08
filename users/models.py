from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    website = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='pics/profile', blank=True)

    def __str__(self):
        return self.user.username


#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UserProfile.objects.create(user=kwargs['instance'])
def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    UserProfile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)
#post_save.connect(create_profile, sender=User)
