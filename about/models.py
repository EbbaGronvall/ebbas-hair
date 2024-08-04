from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stylist(models.Model):
    stylist_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialties = models.CharField(max_length=255)
    price = models.IntegerField()