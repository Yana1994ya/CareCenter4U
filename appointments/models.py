from django.db import models

from users.models import Customer
from centers.models import Center


# Create your models here.

class Appointment(models.Model):
    patient = models.ForeignKey(
        'users.Customer',
        blank=False,
        on_delete=models.CASCADE,
        related_name='u_name'
    )

    time_field = models.TimeField(blank=True, null=True)
    date_field = models.DateField(blank=True, null=True)
    doctor = models.ForeignKey(
        'Doctor',
        max_length=40,
        on_delete=models.CASCADE,
        related_name='doc_name'
    )

    def __str__(self):
        return str(self.patient) + " to doctor " + str(self.doctor)


class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    center_id = models.ForeignKey(Center, blank=False, max_length=100, on_delete=models.CASCADE,
                                  related_name='cen_i_work_at')
    speciality = models.CharField(max_length=200)

    class Meta:
        unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ,' + self.speciality
