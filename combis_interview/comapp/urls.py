from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/mock-fetch/", views.mock_devices, name="fetch-devices"),
    path("api/update-devices/", views.update_devices_view, name="update-devices"),
    path("api/devices/", views.stored_devices_view.as_view(), name="device-list" )
]
