import requests
from .models import Device

def fetch_store():
    external_api_url = "http://127.0.0.1:8000/api/mock-fetch/"
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