from django import forms


class AddAppointment(forms.Form):
    appointment_date = forms.DateField()
    appointment_time = forms.TimeField()
