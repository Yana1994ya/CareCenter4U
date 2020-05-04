from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<id>/', views.detail_view),
    path("add", views.add, name="add"),
    path("edit/<int:app_id>", views.edit, name="edit"),
    path("delete/<int:app_id>", views.delete_app, name='delete'),
    path("view_appointment", views.viewAppointments, name="view_appointment"),

]
