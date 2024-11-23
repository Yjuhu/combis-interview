from django.db import models

# Create your models here.

class Device(models.Model):
    device_id = models.CharField(max_length=50, unique=True)
    hostname = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ])
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"
