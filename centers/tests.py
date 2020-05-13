from django.test import TestCase

# Create your tests here.
from centers.models import City, Neighborhood, Network, Center


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
