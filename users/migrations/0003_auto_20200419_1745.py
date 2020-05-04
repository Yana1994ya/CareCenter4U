import random

from django.db import migrations
from django.contrib.auth.hashers import get_hasher


def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length, 2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


def add_admin_user(apps, schema_editor):
    Customer = apps.get_model('users', 'Customer')

    if not Customer.objects.filter(username="11112222A").count():
        new_admin = Customer()

        new_admin.username = "11112222A"
        new_admin.password = get_hasher().encode("password", random_id(8))
        new_admin.first_name = "admin"
        new_admin.last_name = "admin"
        new_admin.is_superuser = True
        new_admin.is_staff = True
        new_admin.is_active = True
        new_admin.citizen = False
        new_admin.secretary = False
        new_admin.email = "admin@admin.com"
        new_admin.phone_number = 1234567890
        new_admin.address = "admin"
        new_admin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200416_2011'),
    ]

    operations = [
        migrations.RunPython(add_admin_user)
    ]
