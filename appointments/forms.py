from django import forms

from .models import appointments


class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointments
        fields = ['first_name', 'last_name', 'pat_id', 'center', 'time_field', 'date_field', 'doctor_name']



    def clean_first_name(self):
         first_name = self.cleaned_data["first_name"].lower()

         if not first_name.isalpha():
             raise forms.ValidationError("first name shouldn't have digits")

         return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].lower()

        if not last_name.isalpha():
            raise forms.ValidationError("last name shouldn't have digits")

        return last_name

    def clean_pat_id(self):

        full_id = self.cleaned_data["pat_id"]

        if not full_id.isdigit():
            raise forms.ValidationError("ID number should only contain digits")

        return full_id


    def clean_center(self):
         center = self.cleaned_data["center"].lower()

         if not center.isalpha():
             raise forms.ValidationError("center name shouldn't have digits")

         return center

    def clean_date_field(self):
         date_field= self.cleaned_data["date_field"].lower()

         if not date_field.isalpha():
             raise forms.ValidationError("date field shouldn't have digits")

         return date_field

    def clean_doctor_name(self):
         doctor_name = self.cleaned_data["doctor_name"].lower()

         if not doctor_name.isalpha():
             raise forms.ValidationError("doctor name shouldn't have digits")

         return doctor_name

    def clean_time_field(self):
         time_field = self.cleaned_data["time_field"].lower()

         if not time_field.isalpha():
             raise forms.ValidationError("time field shouldn't have digits")

         return time_field
