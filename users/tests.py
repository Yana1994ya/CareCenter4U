from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
from django.test import TestCase

from users.forms import RegistrationForm
from users.models import Customer
from users.views import register


# Create your tests here.
class RegistrationTests(TestCase):
    def setUp(self):
        Customer.objects.create(username='123456780')

        # Unit tests:

    # Unit test #1 - Yana
    # PM2020T15-40
    def test_validate_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number': '123456789'}
        result = form.clean_id_number()
        self.assertEqual(result, '123456789')

    # Unit test #2 - Yana
    # PM2020T15-40
    def test_reject_invalid_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number': '12345678a'}
        self.assertRaises(ValidationError, form.clean_id_number)

    # Unit test #3 - Yana
    # PM2020T15-40
    def test_reject_duplicate_citizen_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number': '123456780'}
        self.assertRaises(ValidationError, form.clean_id_number)

    # Unit test #4 - Yana
    # PM2020T15-40
    def test_validate_secretary_id_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'id_number': '12345678M'}
        result = form.clean_id_number()
        self.assertEqual(result, '12345678M')

    # Unit test #5 - Yana
    # PM2020T15-40
    def test_validate_phone_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'phone_number': '1549357633'}
        result = form.clean_phone_number()
        self.assertEqual(result, '1549357633')

    # Unit test #6 - Yana
    # PM2020T15-40
    def test_reject_invalid_phone_number(self):
        form = RegistrationForm()
        form.cleaned_data = {'phone_number': '154935763a'}
        self.assertRaises(ValidationError, form.clean_phone_number)

    # Unit test #7 - Yana
    # PM2020T15-40
    def test_validate_first_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'first_name': 'tamar'}
        result = form.clean_first_name()
        self.assertEqual(result, 'tamar')

    # Unit test #8 - Yana
    # PM2020T15-40
    def test_reject_invalid_first_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'first_name': 'tamar1'}
        self.assertRaises(ValidationError, form.clean_first_name)

    # Unit test #9 - Yana
    # PM2020T15-40
    def test_validate_last_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'last_name': 'cohen'}
        result = form.clean_last_name()
        self.assertEqual(result, 'cohen')

    # Unit test #10 - Yana
    # PM2020T15-40
    def test_reject_invalid_last_name(self):
        form = RegistrationForm()
        form.cleaned_data = {'last_name': 'cohen1'}
        self.assertRaises(ValidationError, form.clean_last_name)

    # Integration tests:

    # Integration test #1 - Yana
    # PM2020T15-40
    def test_register_citizen(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'id_number': '123456789',
            'password': 'password',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'phone_number': '0501234350',
            'email': 'test@gmail.com',
            'address': '1234',
        }
        # function 1 - preform the register
        response = register(request)
        self.assertIsInstance(response, HttpResponseRedirect)

        # function 2 - Get the registered user
        user = Customer.objects.get(username='123456789')
        self.assertTrue(user.check_password('password'), 'Failed to verify password.')
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.last_name, 'lastname')
        self.assertEqual(user.phone_number, '0501234350')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(user.address, '1234')

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.citizen)
        self.assertFalse(user.secretary)

    # Integration test #2 - Yana
    # PM2020T15-40
    def test_register_secretary(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'id_number': '12345678M',
            'password': 'password',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'phone_number': '0501234350',
            'email': 'test@gmail.com',
            'address': '1234',
        }

        # function 1 - preform the register
        response = register(request)
        self.assertIsInstance(response, HttpResponseRedirect)

        # function 2 - get the registered secretary and assert fields.
        user = Customer.objects.get(username='12345678M')
        self.assertTrue(
            user.check_password('password'),
            'Failed to verify password.'
        )
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.last_name, 'lastname')
        self.assertEqual(user.phone_number, '0501234350')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertEqual(user.address, '1234')

        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.secretary)
        self.assertFalse(user.citizen)

    # Integration test #3 - Yana
    # PM2020T15-40
    def test_reject_invalid_registration_data(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'id_number': '12345678b',
            'password': 'password',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'phone_number': '0501234350',
            'email': 'test@gmail.com',
            'address': '1234',
        }
        # function 1 - attempt to register
        response = register(request)
        self.assertNotIsInstance(response, HttpResponseRedirect)

        # function 2 - Make sure user wasn't registered
        self.assertEqual(Customer.objects.filter(username='12345678b').count(), 0, 'The user was created.')
