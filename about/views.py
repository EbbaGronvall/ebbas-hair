from django.shortcuts import render
from django.views import generic
from .models import Stylist

# Create your views here.

class StylistList(generic.ListView):
    queryset = Stylist.objects.all()
    template_name = "about/about.html"