from django.db import models
from django.contrib.auth.models import User

class Tablet(models.Model):
    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.model_number})"

class UserTablet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE)
    alarm_time = models.TimeField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user.username} - {self.tablet.name} at {self.alarm_time}"
