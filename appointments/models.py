from django.db import models

from users.models import Customer
from centers.models import Center


# Create your models here.

class appointments(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pat_id = models.ForeignKey('users.Customer', default=Customer.USERNAME_FIELD, blank=False, on_delete=models.CASCADE,
                               related_name='u_name')
    center = models.ForeignKey(Center, blank=False, max_length=100, on_delete=models.CASCADE, related_name='cen_id')
    time_field = models.TimeField(blank=True, null=True)
    date_field = models.DateField(blank=True, null=True)
    doctor_name = models.ForeignKey('Doctors', max_length=40, on_delete=models.CASCADE, related_name='doc_name')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.pat_id.username


class Doctors(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    center_id = models.ForeignKey('Centers', blank=False, max_length=100, on_delete=models.CASCADE,
                                  related_name='cen_i_work_at')
    specielity = models.CharField(max_length=200)

    class Meta:
        unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ,' + self.specielity
