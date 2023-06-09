from django.contrib import admin
from .models import Devices, UserDevices, Schedules

# Register your models here.
admin.site.register(Devices)
admin.site.register(UserDevices)
admin.site.register(Schedules)