from django.shortcuts import render
import requests
import responses
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

@responses.activate
def mock_devices_api():
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
    responses.add(
        responses.GET,
        "http://mockapi/devices",
        json=devices,
        status=200
    )

def fetch_devices(request):
    external_api_url = "http://mockapi/devices"
    response = requests.get(external_api_url)
    
    if response.status_code == 200:
        external_data = response.json()
        parsed_data = [
            {
                "device_id": device["id"],
                "hostname": device["name"],
                "ip_address": device["ip"],
                "status": device["state"],
                "location": device["place"],
            }
            for device in external_data
        ]
        return JsonResponse(parsed_data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch devices'}, status=500)
