from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from booking.models import Booking, TIME_CHOICES
from booking.forms import BookingForm
from .forms import EmailUpdateForm
from datetime import datetime
from django.http import HttpResponseRedirect


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
        email_form = EmailUpdateForm(instance=user)

    # Return a dictionary with context data
    return {
        'email_form': email_form,
        'current_email': user.email
    }


@login_required
def update_booking(request):
    user = request.user
    bookings = Booking.objects.filter(customer=user)

    booking_forms = {booking.id: BookingForm(instance=booking) for booking in
                     bookings}

    if request.method == 'POST':
        if 'update_booking' in request.POST:
            booking_id = request.POST.get('booking_id')
            new_day = request.POST.get('new_day')
            new_time = request.POST.get('new_time')
            booking = get_object_or_404(Booking, id=booking_id, customer=user)

            # Convert new_day to a datetime object and check if it's a weekend
            new_day_date = datetime.strptime(new_day, '%Y-%m-%d').date()
            if new_day_date.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
                messages.error(request, 'You cannot book an appointment on a' +
                                        ' weekend.')
            elif Booking.objects.filter(day=new_day, time=new_time,
                                        stylist=booking.stylist).exists():
                messages.error(request, 'The selected time slot is already' +
                                        'booked.')
            else:
                booking.day = new_day_date
                booking.time = new_time
                booking.save()
                messages.success(request, 'Your booking has been updated.')
                return redirect('mypage')
        elif 'delete_booking' in request.POST:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id, customer=user)
            booking.delete()
            messages.success(request, 'Your booking has been deleted.')
            return redirect('mypage')
    else:
        booking_forms = {booking.id: BookingForm(instance=booking) for booking
                         in bookings}

    # Return a dictionary with context data
    return {
        'bookings': bookings,
        'booking_forms': booking_forms,
        'time_choices': TIME_CHOICES,
        'date_today': datetime.now().date(),
    }


@login_required
def mypage(request):
    email_context = update_email(request)
    if isinstance(email_context, HttpResponseRedirect):
        return email_context

    booking_context = update_booking(request)
    if isinstance(booking_context, HttpResponseRedirect):
        return booking_context

    # Combine contexts if neither is a redirect
    context = {**email_context, **booking_context}

    return render(request, 'mypage/mypage.html', context)
