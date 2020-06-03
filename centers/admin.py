from django.contrib import admin
from django import forms

from appointments.models import Doctor
from centers.models import Center, City, Network, Neighborhood


class CenterModelForm(forms.ModelForm):
    hours = forms.CharField(widget=forms.Textarea(attrs={'class': 'rtl'}), required=False)
    routes = forms.CharField(widget=forms.Textarea(attrs={'class': 'rtl'}), required=False)
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rtl w260'}),
        max_length=200
    )

    class Meta:
        model = Center
        exclude = ()


class DoctorInline(admin.TabularInline):
    model = Doctor


class CenterAdmin(admin.ModelAdmin):
    list_display = (
        'city_name', 'neighborhood', 'network', 'name'
    )
    list_display_links = ('name', )
    list_filter = (
        'neighborhood__city',
        'neighborhood',
        'network'
    )

    form = CenterModelForm

    inlines = [
        DoctorInline,
    ]

    class Media:
        css = {
            "all": ("css/admin.css",)
        }


admin.site.register(Center, CenterAdmin)


class CityAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)


class NetworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Network, NetworkAdmin)


class NeighborhoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Neighborhood, NeighborhoodAdmin)
