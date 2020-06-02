from django.shortcuts import render
from users.forms import RegistrationForm, UpdateInfoForm
from users.models import Customer
from centers.models import Center
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_customer = Customer()

            # Stock django User model fields
            new_customer.username = data['id_number']
            new_customer.set_password(data['password'])
            new_customer.first_name = data['first_name']
            new_customer.last_name = data['last_name']
            new_customer.email = data['email']

            # Our custom properties
            new_customer.phone_number = data['phone_number']
            new_customer.address = data['address']
            if new_customer.username.endswith('M'):
                new_customer.secretary = True
            else:
                new_customer.citizen = True
            new_customer.save()

            return HttpResponseRedirect(reverse("register_thanks"))
    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})


def register_thanks(request):
    return render(request, "users/register_thanks.html")

def help_update(request, id_):
    query_results = Customer.objects.get(id=id_)
    return render(request, 'users/help_update.html', {'query_results': query_results})

def update_success(request):
    return render(request, "users/update_success.html")

def update(request, user_id):
    user = Customer.objects.get(id=user_id)
    phone_number = user.phone_number
    address = user.address
    mail = user.email
    
    if request.method != 'POST':
        form = UpdateInfoForm(instance=user)
    else:
        form = UpdateInfoForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("update_success"))
    context = {'phone_number':phone_number, 'address':address, 'email':mail, 'form': form}
    return render(request, 'users/update.html', context)




def show(request, id):
    center = Center.objects.get(id=id)
    return render(request, 'users/show.html', context={'center':center})
