from tkinter.constants import CASCADE

from django.contrib.auth.models import User
from django.db import models
from games.models import RouletteSpin
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='birthday')
    balance = models.IntegerField(default=500, verbose_name='balance')
