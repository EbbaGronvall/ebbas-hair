from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from booking.models import Booking, TIME_CHOICES
from booking.forms import BookingForm
from .forms import EmailUpdateForm
from datetime import datetime

@login_required
def mypage(request):
    user = request.user
    bookings = Booking.objects.filter(customer=user)

    if request.method == 'POST':
        if 'email' in request.POST:
            # Handle email update
            email_form = EmailUpdateForm(request.POST, instance=user)
            if email_form.is_valid():
                email_form.save()
                messages.success(request, 'Your email has been updated.')
                return redirect('mypage')
        elif 'update_booking' in request.POST:
            # Handle booking update
            booking_id = request.POST.get('booking_id')
            new_day = request.POST.get('new_day')
            new_time = request.POST.get('new_time')
            booking = get_object_or_404(Booking, id=booking_id, customer=user)

            if Booking.objects.filter(day=booking.day, time=new_time).exists():
                messages.error(request, 'The selected time slot is already booked.')
            else:
                booking.day = new_day
                booking.time = new_time
                booking.save()
                messages.success(request, 'Your booking has been updated.')
                return redirect('mypage')
        elif 'delete_booking' in request.POST:
            # Handle booking deletion
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id, customer=user)
            booking.delete()
            messages.success(request, 'Your booking has been deleted.')
            return redirect('mypage')
    else:
        email_form = EmailUpdateForm(instance=user)
        booking_forms = {booking.id: BookingForm(instance=booking) for booking in bookings}

    context = {
        'email_form': EmailUpdateForm,
        'booking_forms': BookingForm,
        'bookings': bookings,
        'time_choices': TIME_CHOICES,
        'date_today': datetime.now().date(),
    }
    return render(request, 'mypage/mypage.html', context)