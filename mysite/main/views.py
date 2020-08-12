from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Business, UserData
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, NewBusinessForm, BusinessForm
import datetime
import requests
import json
from .serializers import BusinessSerializer
from rest_framework import viewsets
from .maps import *

def homepage(request):
    return render(request = request, template_name='home.html')


# def homepage(request):
#     d1 = datetime.date.today()
#     d2 = d1 + datetime.timedelta(days=100)
#     e = Event.objects.filter(event_date__gte=d1, event_date__lte=d2).order_by('event_date')
#     return render(request = request,
#                   template_name='main/home.html',
#                   context = {"events": e})

# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"New Account Created:{username}")
#             username = form.cleaned_data.get('username')
#             login(request, user)
#             return redirect("main:homepage")
#         else:
#             for msg in form.error_messages:
#                 messages.error(request, f"{msg}: {form.error_messages[msg]}")

#     form = NewUserForm
#     return render(request = request,
#                   template_name = "register.html",
#                   context={"form":form})

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all().order_by('id')
    serializer_class = BusinessSerializer


def view_local(request):
    if request.user.is_authenticated:
        user = request.user
        b = Business.objects.all()

        data = []
        # hack around for image names
        for i in b:
            x = str(i.b_image).replace('main/static/', '')
            i.image_url = x
            print(user)
            i.distance = get_distance((i.lat, i.long), (user.UserData.lat, user.UserData.long))
            print(user.UserData.lat, user.UserData.long)
            data.append(i)


        # VERY DOGILY SORT BY LOCATION
        i = 1
        while i in range(1, len(data)):
            x2 = data[i].distance
            x1 = data[i-1].distance
            if x1 > x2:
                tmp = data[i-1]
                data[i-1] = data[i]
                data[i] = tmp
                print('yo')  
            i = i + 1
            
        return render(request = request,
                    template_name='view_local.html',
                    context = {"business": data})
    return redirect('')

def user(request):
    if request.user.is_authenticated:
        un = request.user.get_username()
        em = request.user.email
        dj = request.user.date_joined
        p = {"username":un,
            "email":em,
            "date_joined":dj
            }
        return render(request = request, template_name='user.html', context = {"p": p})
        
    else:
        HttpResponseRedirect("/login")




def venue_details(request):
    if request.method == "GET":
        r = request.GET.get('idnumber')
        r = int(r)
        o = Business.objects.get(id=r)
        #return HttpResponse(o.name)
        return render(request = request,
            template_name='venue_details.html',
            context = {"venue": o})

def new_business(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BusinessForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            return render(request=request, template_name="business_created.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created:{username}")
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form}) 

def logout_request(request):
    logout(request)
    messages.success(request, "Logged out :)")
    return redirect("main:homepage")
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def update_coordinates(request):
    temp_set_coordinates()
    return HttpResponse("Done")

# def add_event(request):
#     if request.method == 'POST' and request.user is not None:
#         name = request.POST['event_name']
#         des = request.POST['event_description']
#         date = datetime.datetime.now()
#         host = request.user.username
#         #TODO ADD CONTENT SANITISATION
#         e = Event()
#         e.set_attributes(name, des, date, host)
#         e.save()
#         messages.success(request, "Added Event Successfully")
#         return redirect("main:homepage")
#     else:
#         form = NewEventForm()
#         return render(request = request,
#                     template_name = "main/addevent.html",
#                     context={"form":form})

# def userpage(requeast):
#     if request.user is not None:
#         e = Event.objects.filter(event_hostname=request.user.username)
#         count = e.count()
#         return render(request = request,
#                     template_name = "main/user.html",
#                     context={"username":request.user.username, "events":e, "count":count})


def update_address(request):
    #Updates the address of a user account
    pass