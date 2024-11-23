from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'hostname', 'ip_address', 'status', 'location')
    search_fields = ('device_id', 'hostname', 'ip_address', 'location')
    list_filter = ('status', 'location')

