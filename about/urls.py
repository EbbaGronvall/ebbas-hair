from . import views
from django.urls import path

urlpatterns = [
    path('', views.StylistList.as_view() , name='about')
]