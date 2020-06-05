from json import loads
from unittest.mock import Mock

from django.test import TestCase

# Create your tests here.
from appointments.models import Doctor
from appointments.tests import TestData
from centers.models import City, Neighborhood, Network, Center
from centers.views import cities_json, doctors_json, centers_json


class ModelsTestCase(TestCase):
    # unit tests

    # Unit test #1 - Yana
    # PM2020T15-34
    def test_neighborhood_visible(self):
        city = City(name="Tel Aviv")
        neighborhood = Neighborhood(city=city, name="Center", visible=False)

        self.assertTrue("Center" not in str(neighborhood))

    # Unit test #2 - Yana
    # PM2020T15-34
    def test_city_name_property(self):
        city = City(name="Tel Aviv")
        neighborhood = Neighborhood(city=city, name="Center", visible=False)
        network = Network(name="Macabbi")

        center = Center(
            name="Gahha",
            neighborhood=neighborhood,
            address="Sdarot Moshea Dayan 13",
            network=network,
            hours="09:00-17:00",
            phone="04-23467890",
        )

        self.assertEqual(center.city_name, "Tel Aviv")


# Integration tests
class ModelsIntegrationTestCase(TestCase):
    def setUp(self) -> None:
        self.city_tel_aviv = City(name="Tel Aviv")
        self.city_tel_aviv.save()

        self.city_ashdod = City(name="Ashdod")
        self.city_ashdod.save()

        self.neighborhood_tel_aviv = Neighborhood(city=self.city_tel_aviv, name="Center", visible=False)
        self.neighborhood_tel_aviv.save()

        self.network = Network(name="Macabbi")
        self.network.save()

    def add_center1(self) -> Center:
        center = Center(
            name="Gahha",
            neighborhood=self.neighborhood_tel_aviv,
            address="Sdarot Moshea Dayan 13",
            network=self.network,
            hours="09:00-17:00",
            phone="04-23467890",
            fax="04-23467890",
            email="test@test.com",
            routes="Bus 12"
        )

        center.save()

        return center

    def add_center2(self) -> Center:
        center = Center(
            name="Wall",
            neighborhood=self.neighborhood_tel_aviv,
            address="Herzel 1",
            network=self.network,
            hours="09:00-17:00",
            phone="04-57421812",
            fax="04-23567868",
            email="test2@test2.com",
            routes="Bus 35"
        )

        center.save()

        return center

    # Integration test #1 - Yana
    # PM2020T15-34
    def test_search_by_city(self):
        # function 1 - save the center into the database
        self.add_center1()

        # function 2 - test if we can find the center in Tel Aviv
        self.assertTrue(Center.objects.filter(neighborhood__city=self.city_tel_aviv).exists())

        # function 3 - test if the center is not visible for a search in Ashdod
        self.assertFalse(Center.objects.filter(neighborhood__city=self.city_ashdod).exists())

    # Integration test #2 - Yana
    # PM2020T15-34
    def test_delete_a_center(self):
        # function 1 - save the center into the database
        center = self.add_center1()

        # function 2 - test if we can find the center in Tel Aviv
        self.assertTrue(Center.objects.filter(neighborhood__city=self.city_tel_aviv).exists())

        # function 3 - delete the center
        center.delete()

        # function 4 - test that we can no longer find the center in Tel Aviv
        self.assertFalse(Center.objects.filter(neighborhood__city=self.city_tel_aviv).exists())

    # Integration test #3 - Yana
    # PM2020T15-34
    def test_find_centers_by_neighborhood(self):
        # function 1 - save the center1 into the database
        self.add_center1()

        # function 2 - save the center2 into the database
        self.add_center2()

        # function 3 - test that both centers are accessible via neighborhood
        self.assertEqual(self.neighborhood_tel_aviv.center_set.count(), 2)

    # Integration test #4 - Yana
    # PM2020T15-34
    def test_find_centers_by_network(self):
        # function 1 - save the center1 into the database
        self.add_center1()

        # function 2 - save the center2 into the database
        self.add_center2()

        # function 3 - test that both centers are accessible via neighborhood
        self.assertEqual(self.network.center_set.count(), 2)

    # Integration test #5 - Yana
    # PM2020T15-34
    def test_find_centers_by_city(self):
        # function 1 - save the center1 into the database
        self.add_center1()

        # function 2 - save the center2 into the database
        self.add_center2()

        # function 3 - test that both centers are accessible via city
        self.assertEquals(Center.objects.filter(neighborhood__city=self.city_tel_aviv).count(), 2)

    # Unit test #4 - Yana
    # Sprint3/4
    def test_serialize_city_to_json(self):
        city = City(name="beer_shava", id=10)
        self.assertEqual(city.to_json(), {'id': 10, 'name': 'beer_shava'})

    # Unit test #5 - Yana
    # Sprint3/4
    def test_serialize_doctor_to_json(self):
        test_data = TestData.create()
        test_data.save()

        doc = Doctor(first_name="aharon", last_name="barak", speciality="general", center=test_data.center)
        doc.save()

        self.assertEqual(doc.to_json(), {
            'center_id': 1,
            'first_name': 'aharon',
            'id': 2,
            'last_name': 'barak',
            'speciality': 'general'
        })


class ApiIntegrationTests(TestCase):
    def setUp(self) -> None:
        self.test_data = TestData.create()
        self.test_data.save()

    def assertJson(self, response, content):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(loads(response.content), content)

    # Integration #1 - Yana
    # Sprint3/4
    def test_cities_api(self):
        request = Mock()

        response = cities_json(request)
        self.assertJson(response, [{"id": 1, "name": "test"}])

    # Integration #2 - Yana
    # Sprint3/4
    def test_doctors_api(self):
        request = Mock(GET={})

        response = doctors_json(request)
        self.assertJson(response, [{'center_id': 1,
                                    'first_name': 'first_name',
                                    'id': 1,
                                    'last_name': 'last_name',
                                    'speciality': 'speciality'}])

    # Integration #3 - Yana
    # Sprint3/4
    def test_doctors_api_limit_center(self):
        request = Mock(GET={"center": self.test_data.center.id})

        center = Center(
            neighborhood=self.test_data.neighborhood,
            name="test",
            hours="hours",
            phone="phone",
            fax="fax",
            email="email",
            routes="routes",
            network=self.test_data.network
        )
        center.save()
        doctor = Doctor(center=center, first_name="first_name2", last_name="last_name2", speciality="speciality")
        doctor.save()

        response = doctors_json(request)
        self.assertJson(response, [{'center_id': 1,
                                    'first_name': 'first_name',
                                    'id': 1,
                                    'last_name': 'last_name',
                                    'speciality': 'speciality'}])

    # Integration #4 - Yana
    # Sprint3/4
    def test_centers_api(self):
        request = Mock(GET={}, POST={}, method="GET")

        response = centers_json(request)
        self.assertJson(response, [{'address': '',
                                    'id': 1,
                                    'lat': None,
                                    'long': None,
                                    'name': 'test'}])

    # Integration #5 - Yana
    # Sprint3/4
    def test_centers_filter_api(self):
        city = City(name="test")
        city.save()

        neighborhood = Neighborhood(name="test", city=city)
        neighborhood.save()

        center = Center(
            neighborhood=neighborhood,
            name="test2",
            hours="hours",
            phone="phone",
            fax="fax",
            email="email",
            routes="routes",
            network=self.test_data.network
        )
        center.save()

        request = Mock(GET={"city": self.test_data.city.id}, POST={}, method="GET")

        response = centers_json(request)
        self.assertJson(response, [{'address': '',
                                    'id': 1,
                                    'lat': None,
                                    'long': None,
                                    'name': 'test'}])
