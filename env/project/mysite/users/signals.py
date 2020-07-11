#method post_save if certain model is saved
from django.db.models.signals import post_save

#sender
from django.contrib.auth.models import User

#receiver
from django.dispatch import receiver

from .models import Profile

""" if User model is saved then it will move to create_profile 
    function if that user was created then create profile objects """

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



# Does the same thing
# @receiver(post_save,sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()