from django.urls import path
from centers.views import index, city_index, center_list, center_view

urlpatterns = [
    path("", index, name="centers_index"),
    path("<int:city_id>/", city_index, name="centers_city_index"),
    path("<int:city_id>-/", center_list, name="center_list"),
    path("<int:city_id>-<int:neighborhood_id>/", center_list, name="center_list"),
    path("center/<int:center_id>", center_view, name="center"),
]
