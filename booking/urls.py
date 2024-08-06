from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingPage.as_view() , name='booking')
]