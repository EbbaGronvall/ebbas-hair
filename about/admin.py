from django.contrib import admin
from .models import Stylist
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Stylist)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('stylist_name', 'speciality', 'price')
    search_fields = ['stylist_name']
    list_filter = ('speciality',)
    summernote_fields = ('bio',)
# Register your models here.

