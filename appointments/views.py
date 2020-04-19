from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from appointments.models import Center, Doctor, Appointment
from appointments.forms import AddAppointment


# Create your views here.
@login_required
def centers(request):
    centers = Center.objects.all()

    return render(request, "appointments/centers.html", {"centers": centers})


@login_required
def show_center(request, center_id):
    center = get_object_or_404(Center, id=center_id)
    drs = Doctor.objects.filter(center=center)

    return render(request, "appointments/center.html", {"center": center, "drs": drs})


@login_required
def add_appointment(request, center_id, doctor_id):
    center = get_object_or_404(Center, id=center_id)
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        form = AddAppointment(request.POST)

        if form.is_valid():
            appointment = Appointment()
            appointment.doctor = doctor
            appointment.center = center

            data = form.cleaned_data
            appointment.appointment_date = data["appointment_date"]
            appointment.appointment_time = data["appointment_time"]
            appointment.patient = request.user

            appointment.save()

            return HttpResponseRedirect(reverse("appointments_add_thanks"))

    else:
        form = AddAppointment()

    return render(request, "appointments/add.html", {"center": center, "doctor": doctor, "form": form})


def message(request, text):
    return render(request, "appointments/message.html", {"text": text})
