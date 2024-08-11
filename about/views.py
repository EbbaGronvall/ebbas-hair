from django.shortcuts import render
from django.views import generic
from .models import Stylist


class StylistList(generic.ListView):
    queryset = Stylist.objects.filter(active=True)
    template_name = "about/about.html"
    