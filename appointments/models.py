from django.db import models

# Create your models here.
from users.models import Customer
from centers.models import Center


class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    center = models.ForeignKey(Center, blank=False, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ,' + self.speciality


class Appointment(models.Model):
    patient = models.ForeignKey('users.Customer', blank=False, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, blank=False, on_delete=models.CASCADE)
    appointment_time = models.TimeField(blank=False)
    appointment_date = models.DateField(blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return "<Appointment #%d>" % (
            self.id
        )



