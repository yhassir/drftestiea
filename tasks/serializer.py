from rest_framework import serializers
from .models import Devices, UserDevices, Schedules

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'channel', 'ch_date', 'start_time', 'end_time', 'user_device')
#         model = Schedules
#         # fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'id_device')
        model = Devices

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_device', 'user_age', 'user_genre', 'device')
        model = UserDevices

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'channel', 'ch_date', 'start_time', 'end_time', 'user_device')
        model = Schedules

