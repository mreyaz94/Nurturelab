from django.contrib import admin
from webapi.models import Advisors_DB,Booking_DB
# Register your models here.

class Advisors_admin(admin.ModelAdmin):
    list_display = ['adv_name', 'adv_id', 'adv_pic']

class Booking_admin(admin.ModelAdmin):
    list_display = ['advisor', 'booking_id', 'booking_time']


admin.site.register(Advisors_DB,Advisors_admin)
admin.site.register(Booking_DB,Booking_admin)
