import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django import forms
from users.models import Customer
from centers.models import Center


class RegistrationForm(forms.Form):
    id_number = forms.CharField(min_length=9, max_length=9)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, max_length=9)

    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)

    phone_number = forms.CharField(min_length=10)
    email = forms.EmailField()

    address = forms.CharField(min_length=4)

    def clean_id_number(self):
        full_id = self.cleaned_data["id_number"]
        if full_id.endswith('M'):
            id_num=full_id[0:-1]
        else:
            id_num=full_id  

        if not id_num.isdigit():
            raise forms.ValidationError("ID number should only contain digits")

        if Customer.objects.filter(username=full_id).exists():
            raise forms.ValidationError("A customer with this ID number is already registered")

        return full_id

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]

        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits")

        return phone_number

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


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number', 'address', 'email']

        # ALL THIS CODE MUST NOT BE IN META
        # sender_email = "addmin3439@gmail.com"
        #
        # receiver_email = "addmin3439@gmail.com"
        #
        # # receiver_email = Customer.email
        # password = "ll121212"
        #
        # message = MIMEMultipart("alternative")
        # message["Subject"] = "Employee details!"
        # message["From"] = sender_email
        # message["To"] = receiver_email
        #
        # text = """\
        # Hi,
        # Employee details in have been successfully updated
        #
        # Good Day!!!
        #
        #  """
        #
        # part1 = MIMEText(text, "plain")
        # part2 = MIMEText(text, "plain_2")
        #
        # message.attach(part1)
        # message.attach(part2)
        #
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        #     server.login(sender_email, password)
        #     server.sendmail(
        #         sender_email, receiver_email, message.as_string()
        #     )

       
class CenterFilterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['id', 'name', 'address', 'neighborhood', 'network', 'hours', 'phone', 'routes', 'fax', 'email' ]
