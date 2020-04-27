from django.db import models
from users.models import Customer
from django.template.defaultfilters import default

# Create your models here.

class appointments(models.Model):
	first_name = models.CharField(max_length=200)
	last_name  = models.CharField(max_length=200)
	pat_id = models.ForeignKey('users.Customer',default=Customer.USERNAME_FIELD, blank=False, on_delete=models.CASCADE, related_name='u_name')
	center = models.ForeignKey('Centers', blank=False, max_length=100, on_delete=models.CASCADE, related_name='cen_id')
	time_field = models.TimeField(blank=True, null=True)
	date_field = models.DateField(blank=True, null=True)
	doctor_name  = models.ForeignKey('Doctors', max_length=40, on_delete=models.CASCADE, related_name='doc_name')
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' ' + self.pat_id


class Doctors(models.Model):
	first_name = models.CharField(max_length=200)
	last_name  = models.CharField(max_length=200)
	center_id = models.ForeignKey('Centers', blank=False, max_length=100, on_delete=models.CASCADE, related_name='cen_i_work_at')
	specielity = models.CharField(max_length=200)
	class Meta:
		unique_together = (("first_name", "last_name"),)
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' ,' + self.specielity

class Centers(models.Model):
	cent_id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	address  = models.CharField(max_length=200)
	neighbrohood = models.CharField(max_length=200)
	HMOname = models.CharField(max_length=200)
	hours = models.CharField(max_length=500)
	contact_info = models.CharField(max_length=200)
	routs = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name + ' ' + self.address + ' ' + self.neighbrohood + '\n' + self.contact_info + '\n' + self.hours + '\n' + self.routs 

	
	
	
	
