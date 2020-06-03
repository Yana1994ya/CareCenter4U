from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Neighborhood(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)

    def __str__(self):
        if self.visible:
            return self.city.name + " - " + self.name
        else:
            return self.city.name


class Network(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(max_length=200)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    hours = models.CharField(max_length=800, default=None, blank=True)

    phone = models.CharField(max_length=200, default=None, blank=True)
    fax = models.CharField(max_length=200, default=None, blank=True)
    email = models.EmailField(max_length=200, default=None, blank=True)

    routes = models.CharField(max_length=200, default=None, blank=True)

    long = models.DecimalField(max_digits=10, decimal_places=8, blank=True, default=None, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, default=None, null=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "long": self.long,
            "lat": self.lat
        }

    @property
    def city_name(self) -> str:
        return self.neighborhood.city.name

    def __str__(self):
        return self.name + ' ' + self.address + ' ' + str(self.neighborhood)
