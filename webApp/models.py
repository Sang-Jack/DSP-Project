from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from django.conf import settings

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

ACTIVITY_LEVEL = [
    ('Sedentary: little or no exercise','Sedentary: little or no exercise'),
    ('Exercise 1-3 times/week','Exercise 1-3 times/week'),
    ('xercise 4-5 times/week','Exercise 4-5 times/week'),
    ('Daily exercise or intense exercise 3-4 times/week','Daily exercise or intense exercise 3-4 times/week')
]


class Profile(models.Model):
    username = models.CharField(max_length=200,blank=True, null=True,)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=5, blank=True, null=True)
    birth_date = models.DateField(null=True,blank=True)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    activitylevel = models.CharField(choices=ACTIVITY_LEVEL,max_length=200, blank=True, null=True)
    
    
