from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from booking.models import Booking, TIME_CHOICES
from booking.forms import BookingForm
from .forms import EmailUpdateForm
from datetime import datetime

@login_required
def update_email(request):
    user = request.user

    if request.method == 'POST' and 'email' in request.POST:
        email_form = EmailUpdateForm(request.POST, instance=user)
        if email_form.is_valid():
            email_form.save()
            messages.success(request, 'Your email has been updated.')
            return redirect('mypage')
    else:
        # Initialize the form with the current user instance
        email_form = EmailUpdateForm(instance=user)

    return {
        'email_form': email_form,
        'current_email': user.email
    }

@login_required
def update_booking(request):
    user = request.user
    bookings = Booking.objects.filter(customer=user)

    if request.method == 'POST':
        if 'update_booking' in request.POST:
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
        booking_forms = {booking.id: BookingForm(instance=booking) for booking in bookings}

    return {
        'bookings': bookings,
        'booking_forms': BookingForm,
        'bookings': bookings,
        'time_choices': TIME_CHOICES,
        'date_today': datetime.now().date(),
    }

@login_required
def mypage(request):
    email_context = update_email(request)
    booking_context = update_booking(request)

    context = {**email_context, **booking_context}

    return render(request, 'mypage/mypage.html', context)