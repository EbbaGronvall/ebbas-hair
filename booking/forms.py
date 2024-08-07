from django import forms
from booking.models import Booking, TIME_CHOICES

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['stylist', 'day', 'time']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['time'].choices = TIME_CHOICES