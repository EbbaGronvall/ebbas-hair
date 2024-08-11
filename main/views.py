from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'main/index.html'
