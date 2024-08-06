from django.db import models
from django.contrib.auth.models import User
from about.models import Stylist
from django.utils import timezone

# Create your models here.



class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_booking")
    stylist = models.ForeignKey(
        Stylist, on_delete=models.CASCADE, related_name="stylist_booking", null=True, blank=True)
    day = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Booking by {self.customer.username} with {self.stylist.stylist_name.username} on {self.day} at {self.time}"