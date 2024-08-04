from . import views
from django.urls import path

urlpatterns = [
    path('', views.stylist_list, name='home')
]