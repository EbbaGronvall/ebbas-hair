from django import forms
from booking.models import Booking, TIME_CHOICES
from datetime import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['stylist', 'day', 'time', 'comment']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Is there anything we need to know about your hair beforehand?'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].choices = TIME_CHOICES

    def clean(self):
        cleaned_data = super().clean()
        stylist = cleaned_data.get("stylist")

        if not stylist:
            raise forms.ValidationError('You must select a stylist.')

        return cleaned_data

    def clean_day(self):
        day = self.cleaned_data.get('day')
        if day < datetime.now().date():
            raise forms.ValidationError('You cannot book an appointment in the past.')
        return day