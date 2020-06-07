from django.contrib import admin
from .models import Customer

admin.site.site_header = 'Admin CateCenter4U'
# Register your models here.

class CustomerA(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')

admin.site.register(Customer, CustomerA)


