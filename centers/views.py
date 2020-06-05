from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from appointments.models import Doctor
from centers.models import City, Neighborhood, Center


# Create your views here.
def index(request):
    return render(
        request,
        'centers/index.html',
        context={
            'cities': City.objects.all()
        },
    )


def city_index(request, city_id):
    city = get_object_or_404(City, id=city_id)

    return render(
        request,
        "centers/city_index.html",
        context={
            "city": city,
            "neighborhoods": city.neighborhood_set.all()
        }
    )


def center_list(request, city_id, neighborhood_id=None):
    city = get_object_or_404(City, id=city_id)
    neighborhood = None

    if neighborhood_id:
        neighborhood = get_object_or_404(city.neighborhood_set, id=neighborhood_id)
        search_list = neighborhood.center_set.all()
    else:
        search_list = Center.objects.filter(neighborhood__city=city).all()

    return render(
        request,
        "centers/centers.html",
        context={
            "city": city,
            "neighborhood": neighborhood,
            "centers": search_list
        }
    )


def center_view(request, center_id):
    center = get_object_or_404(Center, id = center_id)
    return render(
        request,
        "centers/center.html",
        context={
            "center": center
        }
    )


def centers_json(request):
    if request.method == "GET":
        centers = Center.objects.all()

        if "city" in request.GET:
            centers = centers.filter(neighborhood__city__id=request.GET["city"])

        result = []

        for center in centers:
            result.append(center.to_json())

        return JsonResponse(result, safe=False)
    else:
        center_id = int(request.POST["id"])
        long = float(request.POST["long"])
        lat = float(request.POST["lat"])

        center = get_object_or_404(Center, id=center_id)

        center.long = long
        center.lat = lat
        center.save()

        return JsonResponse({"status": "ok"})


def cities_json(request):
    cities = City.objects.all()

    return JsonResponse(list(map(lambda x: x.to_json(), cities)), safe=False)


def doctors_json(request):
    doctors = Doctor.objects.all()

    if "center" in request.GET:
        doctors = doctors.filter(center_id=request.GET["center"])

    return JsonResponse(list(map(lambda x: x.to_json(), doctors)), safe=False)
