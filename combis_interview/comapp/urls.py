from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/fetch-devices/", views.mock_devices, name="fetch-devices"),
    path("api/update-devices/", views.update_devices_view, name="update-devices"),
]
