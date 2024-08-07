from .views import BookingPage
from django.urls import path

urlpatterns = [
    path('', BookingPage, name='booking')
]