from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render
from django.urls import reverse
from django.views.generic import DetailView

from appointments.forms import AppointmentForm, AppointmentSecForm
from appointments.models import Appointment


# after updating it will redirect to detail_View 
def detail_view(request, id):
    context = {}
    context["data"] = Appointment.objects.get(id=id)
    return render(request, "detail_view.html", context)


class appointmentsdetail(DetailView):
    template_name = 'appointment_files/view_appointment.html'
    model = Appointment


def index(request):
    if request.user.is_authenticated:
        # If a user is logged in, redirect them to a page informing them of such
        return render(request, 'appointment_files/index.html')
    else:
        return render(request, 'base.html')


def view_appointments(request):
    query_results = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointment_files/view_appointment.html', {'query_results': query_results})


def view_appointments_sec(request):
    if not request.user.secretary:
        return HttpResponseRedirect("/")

    query_results = Appointment.objects.all()
    filter_id = None
    if request.GET.get("filter_id"):
        filter_id = request.GET["filter_id"]
        query_results = query_results.filter(patient__username=filter_id)

    return render(request, 'appointment_files/view_appointment_sec.html', {
        'query_results': query_results,
        "filter_id": filter_id
    })


def add(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.instance
            appointment.patient = request.user
            appointment.save()

            return HttpResponseRedirect(reverse("appointment_added"))

    else:
        form = AppointmentForm()

    return render(request, "appointment_files/add.html", {"form": form})


def add_sec(request):
    if request.method == "POST":
        form = AppointmentSecForm(request.POST)
        if form.is_valid():
            appointment = form.instance
            appointment.patient = form.cleaned_data["patient"]
            appointment.save()

            return HttpResponseRedirect(reverse("appointment_added"))

    else:
        form = AppointmentSecForm()

    return render(request, "appointment_files/add_sec.html", {"form": form})


def delete_app(request, app_id):
    app = Appointment.objects.get(id=app_id)

    if request.method == 'POST':
        app.delete()

    return HttpResponseRedirect(reverse("appointment_deleted"))


def edit(request, app_id):
    app = Appointment.objects.get(id=app_id)
    f_name = app.first_name
    l_name = app.last_name
    t = app.time_field
    d = app.date_field
    cent = app.center
    d_name = app.doctor_name
    p_id = app.pat_id
    if request.method != 'POST':
        form = AppointmentForm(instance=app)
    else:
        form = AppointmentForm(instance=app, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("appointment edited!!!")
    context = {'first_name': f_name, 'last_name': l_name, 'pat_id': p_id, 'center': cent,
               'time_field': t, 'date_field': d, 'doctor_name': d_name, 'form': form}
    return render(request, 'appointment_files/edit.html', context)
