from django.shortcuts import render
from django.http import JsonResponse
from . import utils

# Create your views here.

def home(request):
    return render(request, "home.html")

# Mock API endpoint
def mock_devices(request):
    # Simulated device data
    devices = [
        {
            "device_id": "abc123",
            "hostname": "Switch01",
            "ip_address": "192.168.1.1",
            "status": "active",
            "location": "Data Center A"
        },
        {
            "device_id": "def456",
            "hostname": "Router02",
            "ip_address": "192.168.1.2",
            "status": "inactive",
            "location": "Data Center B"
        }
    ]
    return JsonResponse(devices, safe=False)

# Update/Store API
def update_devices_view(request):
    result = utils.fetch_store()
    return JsonResponse(result)