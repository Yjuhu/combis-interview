from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import Device

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

def fetch_store():
    external_api_url = "http://127.0.0.1:8000/api/fetch-devices/"
    response = requests.get(external_api_url)
    
    if response.status_code == 200:
        devices_data = response.json()
        
        for device_data in devices_data:
            # Update or Create
            obj, created = Device.objects.update_or_create(
                device_id = device_data["device_id"],
                defaults = {
                    "hostname": device_data["hostname"],
                    "ip_address": device_data["ip_address"],
                    "status": device_data["status"],
                    "location": device_data["location"],
                }
            )
            if created:
                print(f"Created new device: {obj.device_id}")
            else:
                print(f"Updated existing device: {obj.device_id}")
        return {"status": "success", "message": "Devices saved/updated successfully."}
    else:
        print("Error fetching devices")
        return {"status": "error", "message": "Error fetching devices"}
