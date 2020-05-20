from django.test import TestCase
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
import datetime
# Create your tests here.
from .forms import appointmentForm
from .models import Doctors, appointments
from appointments.views import add, edit, detail_view, appointmentsdetail, index


class DoctorsTest(TestCase):
    def setUpTestdata(cls):
        Doctors.objects.create(first_name = 'lio')
        appointments.objects.create(app = '1234')

    def test_validate_first_name(self):
        form = appointmentForm()
        form.cleaned_data = {'first_name': 'tamar'}
        result = form.clean_first_name()
        self.assertEqual(result, 'tamar')

    def test_reject_invalid_first_name(self):
        form = appointmentForm()
        form.cleaned_data = {'first_name': 'tamar1'}
        self.assertRaises(ValidationError, form.clean_first_name)

    def test_validate_last_name(self):
        form = appointmentForm()
        form.cleaned_data = {'last_name': 'cohen'}
        result = form.clean_last_name()
        self.assertEqual(result, 'cohen')

    def test_reject_invalid_last_name(self):
        form = appointmentForm()
        form.cleaned_data = {'last_name': 'cohen1'}
        self.assertRaises(ValidationError, form.clean_last_name)

    def test_validate_pat_id(self):
        form = appointmentForm()
        form.cleaned_data = {'pat_id': '123123'}
        result = form.clean_pat_id()
        self.assertEqual(result, '123123')

    def test_reject_invalid_pat_id(self):
        form = appointmentForm()
        form.cleaned_data = {'last_name': 'cohen1'}
        self.assertRaises(ValidationError, form.clean_last_name)


    def test_validate_center(self):
        form = appointmentForm()
        form.cleaned_data = {'center': 'maccbi'}
        result = form.clean_center()
        self.assertEqual(result, 'maccbi')

    # def test_reject_invalid_center(self):
    #     form = appointmentForm()
    #     form.cleaned_data = {'center': 'Maccbi1'}
    #     self.assertRaises(ValidationError, form.clean_center)

    def test_validate_date_field(self):
        form = appointmentForm()
        form.cleaned_data = {'date_field': 'here'}
        result = form.clean_date_field()
        self.assertEqual(result, 'here')



    def test_validate_doctor_name(self):
        form = appointmentForm()
        form.cleaned_data = {'doctor_name': 'tamar'}
        result = form.clean_doctor_name()
        self.assertEqual(result, 'tamar')


    def test_Docter(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            # 'first_name':'first_name',
            # 'last_name':'last_name',
            # 'pat_id':'pat_id',
            # 'center':'center',
            # 'time_field''date_field''doctor_name'

            # 'form':'1234',
            # 'app':'1234',
            # 'f_name':'firstname',
            # 'l_name':'lastname',
            # 't': '12-12-2012',
            # 'd': '12-12-2012',
            # 'cent':'maccbi',
            # 'd_name': 'doctor_name',
            # 'p_id': '12341234',
            'id': '12341234',
            'first_name':'firstname',
            'last_name':'lastname',
            'specielity':'specielity',
            'center_id':'maccbi',

        }
        response = Doctors(request)
        # self.assertIsInstance(response, HttpResponseRedirect)
        # appo = appointments.objects.get(first_name = 'lio')
        # self.assertEqual(appo.first_name, 'firstname')
        # self.assertEqual(appo.last_name, 'lastname')


