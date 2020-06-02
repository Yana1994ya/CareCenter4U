from django import forms

from appointments.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient',  'time_field', 'date_field', 'doctor']

    def clean_patient(self):

        full_id = self.cleaned_data["patient"]

        if not full_id.isdigit():
            raise forms.ValidationError("ID number should only contain digits")

        return full_id

    def clean_date_field(self):
         date_field = self.cleaned_data["date_field"].lower()

         if not date_field.isalpha():
             raise forms.ValidationError("date field shouldn't have digits")

         return date_field

    def clean_doctor(self):
         doctor = self.cleaned_data["doctor"].lower()

         if not doctor.isalpha():
             raise forms.ValidationError("doctor name shouldn't have digits")

         return doctor

    def clean_time_field(self):
         time_field = self.cleaned_data["time_field"].lower()

         if not time_field.isalpha():
             raise forms.ValidationError("time field shouldn't have digits")

         return time_field
