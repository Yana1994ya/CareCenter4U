from django import forms
from users.models import Customer
from django.core.validators import RegexValidator

class RegistrationForm(forms.Form):
    tehudatExpression= RegexValidator(r'\d{8}(M|A)?$', 'Please input a correct ID pattern. IE:8 digits only or 8 digits + M or A')
    id_number = forms.CharField(min_length=8, max_length=9,validators=[tehudatExpression])
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=9)

    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)

    phone_number = forms.CharField(min_length=10)
    email = forms.EmailField()

    address = forms.CharField(min_length=4)

    def clean_id_number(self):
        id_num = self.cleaned_data["id_number"]

#         if not id_num.isdigit():
#             raise forms.ValidationError("ID number should only contain digits")

        if Customer.objects.filter(username=id_num).exists():
            raise forms.ValidationError("A customer with this ID number is already registered")

        return id_num

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]

        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits")

        return phone_number

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"].lower()

        if first_name.isdigit():
            raise forms.ValidationError("first name shouldn't have digits")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].lower()

        if last_name.isdigit():
            raise forms.ValidationError("last name shouldn't have digits")

        return last_name
    
class LoginForm(forms.Form):
    tehudatExpression= RegexValidator(r'\d{8}(M|A)?$', 'Please input a correct ID pattern. IE:8 digits only or 8 digits + M or A')
    id_number = forms.CharField(min_length=8, max_length=9,validators=[tehudatExpression])
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=9)
    
    def clean_id_number(self):
        id_num = self.cleaned_data["id_number"]
        return id_num
    def clean_password(self):
        password= self.cleaned_data["password"]
        return password
    
    