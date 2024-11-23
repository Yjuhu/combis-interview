from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

# Mock API endpoint
def mock_devices_api(request):
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

def fetch_store(request):
    external_api_url = "http://mockapi/devices"
    response = requests.get(external_api_url)
    
    if response.status_code == 200:
        external_data = response.json()
        parsed_data = [
            {
                "device_id": device["device_id"],
                "hostname": device["hostname"],
                "ip_address": device["ip_address"],
                "status": device["status"],
                "location": device["location"],
            }
            for device in external_data
        ]
        return JsonResponse(parsed_data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch devices'}, status=500)
