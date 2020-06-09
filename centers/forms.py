from django import forms
from centers.models import Center


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['name', 'neighborhood', 'address', 'hours', 'phone', 'fax', 'email']
