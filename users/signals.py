from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# here the user model is the sender
# we built a receiver , that is a function that takes the signal and perform some tasks

# runs everytime a user is created
# post_save is a signal , that is been received by @receiver and the it adds the function functionality to it.
# receiver is a decorator that we add to our function

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if the user was created
    if created:
        # create a user profile object with user equals to the instance of the user that was created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()

# after that we have to import our signals inside of the ready function of our users apps.py 