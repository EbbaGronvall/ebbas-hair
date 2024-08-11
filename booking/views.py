from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from booking.models import Booking, TIME_CHOICES
from booking.forms import BookingForm
from datetime import datetime


@login_required
def BookingPage(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            if Booking.objects.filter(day=booking.day, time=booking.time,
                                      stylist=booking.stylist).exists():
                messages.error(request, 'The selected time slot is already' +
                                        ' booked.')
            else:
                booking.save()
                messages.success(request, 'Your appointment has been booked.')
                return redirect('mypage')
        else:
            # Add form errors to messages
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = BookingForm()

    context = {
        'form': form,
        'time_choices': TIME_CHOICES,
        'date_today': datetime.now().date(),
    }

    return render(request, 'booking/booking.html', context)
