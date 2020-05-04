from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    
    citizen = models.BooleanField(default=False)
    secretary = models.BooleanField(default=False)
