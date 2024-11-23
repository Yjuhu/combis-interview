from django.urls import path
from . import views
from .views import DeviceListAPIView

urlpatterns = [
    path("", views.home, name="home"),
    path('api/fetch-devices/', views.fetch_devices, name='fetch-devices'),
]
