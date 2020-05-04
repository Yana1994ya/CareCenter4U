from django.contrib import admin
from .models import appointments
from appointments.models import Doctors

# Register your models here.
admin.site.register(appointments)


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctors, DoctorAdmin)
