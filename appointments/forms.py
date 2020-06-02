from django import forms
from datetime import datetime, timedelta, time

from django.core.exceptions import ValidationError

from appointments.models import Appointment


def valid_times():
    return_list = []

    runner = datetime(2000, 1, 1, 8, 0, 0)

    while runner.time() < time(13, 0, 0):
        return_list.append((runner.time(), runner.strftime("%H:%M")))
        runner += timedelta(minutes=10)

    return return_list


class AppointmentForm(forms.ModelForm):
    time_field = forms.ChoiceField(choices=valid_times())
    date_field = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    def clean_date_field(self):
        returned_date = self.cleaned_data["date_field"]
        # Don't allow appointments on Sat
        if returned_date.weekday() == 5:
            raise ValidationError("Appointments are not allowed on Saturday")

        return returned_date

    def clean(self):
        doctor = self.cleaned_data["doctor"]
        returned_time = self.cleaned_data["time_field"]
        returned_date = self.cleaned_data["date_field"]

        if Appointment.objects.filter(doctor=doctor, time_field=returned_time, date_field=returned_date).exists():
            raise ValidationError("This appointment slot is taken chose another time")

        return self.cleaned_data

    class Meta:
        model = Appointment
        fields = ['time_field', 'date_field', 'doctor']
