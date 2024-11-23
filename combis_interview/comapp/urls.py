from django.urls import path
from . import views
from .views import DeviceListAPIView

urlpatterns = [
    path("", views.home, name="home"),
    path('api/devices/', DeviceListAPIView.as_view(), name='device-list'),
]
