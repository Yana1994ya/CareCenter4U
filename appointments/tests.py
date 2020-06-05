from dataclasses import dataclass

from django.test import TestCase
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
import datetime
# Create your tests here.
from appointments.forms import AppointmentForm, AppointmentSecForm
from appointments.models import Doctor, Appointment
from appointments.views import add, edit, detail_view, appointmentsdetail, index
from centers.models import City, Neighborhood, Center, Network
from users.models import Customer


@dataclass
class TestData:
    city: City
    neighborhood: Neighborhood
    network: Network
    center: Center
    doctor: Doctor

    @staticmethod
    def create() -> "TestData":
        city = City(name="test")
        neighborhood = Neighborhood(name="test", city=city)
        network = Network(name="test")
        center = Center(
            neighborhood=neighborhood,
            name="test",
            hours="hours",
            phone="phone",
            fax="fax",
            email="email",
            routes="routes",
            network=network
        )
        doctor = Doctor(center=center, first_name="first_name", last_name="last_name", speciality="speciality")

        return TestData(
            city=city,
            neighborhood=neighborhood,
            network=network,
            center=center,
            doctor=doctor
        )

    def save(self):
        self.city.save()
        self.neighborhood.save()
        self.network.save()
        self.center.save()
        self.doctor.save()


class DoctorsTest(TestCase):
    def setUpTestdata(cls):
        Doctor.objects.create(first_name = 'lio')
        Appointment.objects.create(app = '1234')

    def test_validate_first_name(self):
        form = AppointmentForm()
        form.cleaned_data = {'first_name': 'tamar'}
        result = form.clean_first_name()
        self.assertEqual(result, 'tamar')

    def test_reject_invalid_first_name(self):
        form = AppointmentForm()
        form.cleaned_data = {'first_name': 'tamar1'}
        self.assertRaises(ValidationError, form.clean_first_name)

    def test_validate_last_name(self):
        form = AppointmentForm()
        form.cleaned_data = {'last_name': 'cohen'}
        result = form.clean_last_name()
        self.assertEqual(result, 'cohen')

    def test_reject_invalid_last_name(self):
        form = AppointmentForm()
        form.cleaned_data = {'last_name': 'cohen1'}
        self.assertRaises(ValidationError, form.clean_last_name)

    def test_validate_pat_id(self):
        form = AppointmentForm()
        form.cleaned_data = {'pat_id': '123123'}
        result = form.clean_pat_id()
        self.assertEqual(result, '123123')

    def test_reject_invalid_pat_id(self):
        form = AppointmentForm()
        form.cleaned_data = {'last_name': 'cohen1'}
        self.assertRaises(ValidationError, form.clean_last_name)

    def test_validate_center(self):
        form = AppointmentForm()
        form.cleaned_data = {'center': 'maccbi'}
        result = form.clean_center()
        self.assertEqual(result, 'maccbi')

    # def test_reject_invalid_center(self):
    #     form = appointmentForm()
    #     form.cleaned_data = {'center': 'Maccbi1'}
    #     self.assertRaises(ValidationError, form.clean_center)

    def test_validate_date_field(self):
        form = AppointmentForm()
        form.cleaned_data = {'date_field': 'here'}
        result = form.clean_date_field()
        self.assertEqual(result, 'here')

    def test_validate_doctor_name(self):
        form = AppointmentForm()
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
        response = Doctor(request)
        # self.assertIsInstance(response, HttpResponseRedirect)
        # appo = appointments.objects.get(first_name = 'lio')
        # self.assertEqual(appo.first_name, 'firstname')
        # self.assertEqual(appo.last_name, 'lastname')

    # Unit test #1 - Yana
    # Sprint3/4
    def test_sec_add_allow_only_citizen(self):
        Customer(username="123456789", citizen=False).save()

        form = AppointmentSecForm()

        form.cleaned_data = {
            "patient": "123456789"
        }
        with self.assertRaises(ValidationError) as ctx:
            form.clean_patient()

        self.assertEqual(ctx.exception.message, "patient ID must be citizen")

    # Unit test #2 - Yana
    # Sprint3/4
    def test_sec_add_allow_only_registered_users(self):
        form = AppointmentSecForm()

        form.cleaned_data = {
            "patient": "123456789"
        }

        with self.assertRaises(ValidationError) as ctx:
            form.clean_patient()
        self.assertEqual(ctx.exception.message, "patient with this ID is not registered")

    # Unit test #3 - Yana
    # Sprint3/4
    def test_do_not_allow_appointments_to_same_time(self):
        patient = Customer(username="123456789", citizen=False)
        patient.save()

        test_data = TestData.create()
        test_data.save()

        date_field = datetime.date(2000, 1, 1)
        time_field = datetime.time(8, 0, 0)

        app = Appointment(doctor=test_data.doctor, date_field=date_field, time_field=time_field, patient=patient)
        app.save()

        form = AppointmentForm()
        form.cleaned_data = {
            "doctor": test_data.doctor,
            "date_field": date_field,
            "time_field": time_field
        }

        with self.assertRaises(ValidationError) as ctx:
            form.clean()
        self.assertEqual(ctx.exception.message, "This appointment slot is taken chose another time")

