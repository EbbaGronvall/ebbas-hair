from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#def index(request):
#    return HttpResponse("Welcome")

class HomePage(TemplateView):
    template_name = 'main/index.html'


