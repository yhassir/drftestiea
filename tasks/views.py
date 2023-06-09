from rest_framework import viewsets
# from .serializer import TaskSerializer, DeviceSerializer, UserDeviceSerializer, SchedulesSerializer
from .serializer import DeviceSerializer, UserDeviceSerializer, SchedulesSerializer
from .models import Devices, UserDevices, Schedules

# Create your views here.
# ----
# class TaskViews(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Schedules.objects.all()

class ScheduleViews(viewsets.ModelViewSet):
    serializer_class = SchedulesSerializer
    queryset = Schedules.objects.all()

class DevicesViews(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Devices.objects.all()

class UserDevicesViews(viewsets.ModelViewSet):
    serializer_class = UserDeviceSerializer
    queryset = UserDevices.objects.all()