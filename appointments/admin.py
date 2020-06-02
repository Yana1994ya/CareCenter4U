from django.contrib import admin
from appointments.models import Doctor, Appointment

# Register your models here.
admin.site.register(Appointment)


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctor, DoctorAdmin)
