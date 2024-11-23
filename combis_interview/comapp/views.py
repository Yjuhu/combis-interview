from django.shortcuts import render
from django.http import JsonResponse
from . import utils
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer

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

# Stored Devices List Rest API
class stored_devices_view(APIView):
    def get(self, request):
        # Fetch devices with optional status filtering
        status = request.query_params.get('status')  # DRF query params

        if status in ['active', 'inactive']:
            devices = Device.objects.filter(status=status)
        else:
            devices = Device.objects.all()

        # Serialize and return the response
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)