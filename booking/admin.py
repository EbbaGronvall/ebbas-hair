from django.contrib import admin
from .models import Booking, Stylist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('stylist', 'customer', 'day', 'time')
    search_fields = ['stylist', 'customer', 'day', 'time']
    list_filter = ('stylist', 'day')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "stylist":
            kwargs["queryset"] = Stylist.objects.filter(active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register your models here.

