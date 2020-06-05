from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from appointments import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<id>/', views.detail_view),
    path("add", views.add, name="add"),
    path("add_sec", views.add_sec, name="appointment_add_sec"),
    path("added", TemplateView.as_view(template_name="appointment_files/added.html"), name="appointment_added"),
    path("edit/<int:app_id>", views.edit, name="edit"),
    path("delete/<int:app_id>", views.delete_app, name='delete'),
    path("view_appointment", views.view_appointments, name="view_appointment"),
    path("view_appointment_sec", views.view_appointments_sec, name="view_appointment_sec"),
    path("deleted", TemplateView.as_view(template_name="appointment_files/deleted.html"), name="appointment_deleted")

]
