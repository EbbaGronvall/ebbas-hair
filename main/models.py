from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stylist(models.Model):
    stylist_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialties = models.CharField(max_length=255)
    price = models.IntegerField()


class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_booking")
    stylist = models.ForeignKey(
        Stylist, on_delete=models.CASCADE, related_name="stylist_booking", null=True, blank=True)
    appointment = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
