from django.test import TestCase

# Create your tests here.
from centers.models import City, Neighborhood, Network, Center


class ModelsTestCase(TestCase):
    # unit tests
    def test_neighborhood_visible(self):
        city = City(name="Tel Aviv")
        neighborhood = Neighborhood(city=city, name="Center", visible=False)

        self.assertTrue("Center" not in str(neighborhood))

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
    def test_search_by_city(self):
        city_tel_aviv = City(name="Tel Aviv")
        city_tel_aviv.save()
        city_ashdod = City(name="Ashdod")
        city_ashdod.save()

        neighborhood_tel_aviv = Neighborhood(city=city_tel_aviv, name="Center", visible=False)
        neighborhood_tel_aviv.save()

        network = Network(name="Macabbi")
        network.save()

        Center(
            name="Gahha",
            neighborhood=neighborhood_tel_aviv,
            address="Sdarot Moshea Dayan 13",
            network=network,
            hours="09:00-17:00",
            phone="04-23467890",
            fax="04-23467890",
            email="test@test.com",
            routes="Bus 12"
        ).save()

        # test if we can find the center in Tel Aviv
        self.assertTrue(Center.objects.filter(neighborhood__city=city_tel_aviv).exists())

        # test if the center is not visible for a search in Ashdod
        self.assertFalse(Center.objects.filter(neighborhood__city=city_ashdod).exists())
