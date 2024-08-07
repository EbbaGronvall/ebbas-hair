from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking, TIME_CHOICES
from datetime import datetime

# Create your views here.

@login_required
def BookingPage(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            if Booking.objects.filter(day=booking.day, time=booking.time, stylist=booking.stylist).exists():
               messages.error(request, 'The selected time slot is already booked.')
            else:
                booking.save()
                messages.success(request, 'Your appointment has been booked.')
                return redirect('mypage')
    else:
        form = BookingForm()
    context = {
        'form': BookingForm,
        'time_choices': TIME_CHOICES,
        'date_today': datetime.now().date(),
    } 
    return render(request, 'booking/booking.html', context)

