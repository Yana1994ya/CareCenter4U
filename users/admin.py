from django.contrib import admin
from .models import Customer

admin.site.site_header = 'Admin CateCenter4U'
# Register your models here.

admin.site.register(Customer)