from django.db import models
from django.contrib.auth.models import User
from about.models import Stylist
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.


TIME_CHOICES = (
        ('10:00', '10:00'),
        ('11:30', '11:30'),
        ('13:00', '13:00'),
        ('14:30', '14:30'),
        ('16:00', '16:00'),
        ('17:30', '17:30'),
)
      

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_booking")
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name="stylist_booking", null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10:00")
    comment = models.TextField(max_length=150, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure the requested day is not in the past
        if self.day < datetime.now().date():
            raise ValidationError('Bookings cannot be made in the past.')
        # Ensure the booking day is a weekday
        if self.day.weekday() >= 5: 
            raise ValidationError('Bookings can only be made on weekdays.')
        # Ensure the time slot is available
        if Booking.objects.filter(day=self.day, time=self.time, stylist=self.stylist).exists():
            raise ValidationError('The selected time slot is already booked for this stylist.')

    def __str__(self):
        return f"Booking by {self.customer.username} with {self.stylist.stylist_name.username} on {self.day} at {self.time}"