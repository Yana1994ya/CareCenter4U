from django import forms

from .models import appointments


class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointments
        fields = ['first_name', 'last_name', 'pat_id', 'center', 'time_field', 'date_field', 'doctor_name']
