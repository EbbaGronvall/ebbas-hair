from django import forms
from booking.models import Booking, TIME_CHOICES
from datetime import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['stylist', 'day', 'time', 'comment']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['time'].choices = TIME_CHOICES

        def clean_day(self):
            day = self.cleaned_data.get('day')
            if day < datetime.now().date():
                raise forms.ValidationError('You cannot book an appointment in the past.')
            return day