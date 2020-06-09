import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django import forms
from users.models import Customer
from centers.models import Center


class UpdateInfoForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['name', 'neighborhood', 'address', 'hours', 'phone', 'fax', 'email']