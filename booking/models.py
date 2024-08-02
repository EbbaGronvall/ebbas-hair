from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_booking")
    appointment = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)