from django.urls import path
from appointments.views import centers, show_center, add_appointment, message

urlpatterns = [
    path("", centers, name="appointments_centers"),
    path("center/<center_id>", show_center, name="appointments_center"),
    path("add/<center_id>/<doctor_id>", add_appointment, name="appointments_add"),
    path("add/thanks", message, {"text": "The appointment has been set"}, name="appointments_add_thanks")
]
