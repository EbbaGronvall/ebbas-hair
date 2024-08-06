from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stylist(models.Model):
    stylist_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    speciality = models.CharField(max_length=255)
    price = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.stylist_name.username