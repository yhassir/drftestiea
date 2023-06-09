from django.db import models

# Create your models here.
class Devices(models.Model):
    id_device = models.CharField(max_length=20)

    def __str__(self):
        return self.id_device
    

class UserDevices(models.Model):
    user_device = models.CharField(max_length=50)
    user_age = models.CharField(max_length=20)
    user_genre = models.CharField(max_length=20)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_device + ' ==> ' + self.device.id_device
    

class Schedules(models.Model):
    channel = models.CharField(max_length=100)

    # date format (YYYY-MM-DD)
    ch_date = models.DateField(auto_now = False, auto_now_add = False)

    # time format (HH:MM:SS) to 24 Hrs
    start_time = models.TimeField(auto_now = False, auto_now_add = False)
    end_time = models.TimeField(auto_now = False, auto_now_add = False)
    user_device = models.ForeignKey(UserDevices, on_delete=models.CASCADE)

    def __str__(self):
        return self.channel + ' - ' + str(self.ch_date) + ' ==> ' + self.user_device.user_device