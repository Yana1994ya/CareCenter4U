from django.contrib import admin
from appointments.models import Doctor, Center


# Register your models here.
class CenterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Center, CenterAdmin)


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor, DoctorAdmin)