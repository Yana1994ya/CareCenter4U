from django.urls import path
from django.views.generic import TemplateView

from centers.views import index, city_index, center_list, center_view, centers_json, cities_json, doctors_json, update_center

urlpatterns = [
    path("", index, name="centers_index"),
    path("<int:city_id>/", city_index, name="centers_city_index"),
    path("<int:city_id>-/", center_list, name="center_list"),
    path("<int:city_id>-<int:neighborhood_id>/", center_list, name="center_list"),
    path("center/<int:center_id>", center_view, name="center"),
    path("centers.json", centers_json, name="centers_json"),
    path("cities.json", cities_json, name="cities_json"),
    path("doctors.json", doctors_json, name="doctors_json"),
    path("map", TemplateView.as_view(template_name="centers/map.html"), name="centers_map"),
    path("update_center/<int:center_id>", update_center, name="update_center"),

]
