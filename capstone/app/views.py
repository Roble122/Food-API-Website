"""
Definition of views.
"""

from datetime import datetime
from urllib.error import HTTPError
from django.shortcuts import render, redirect
from .forms import NewUserForm, YelpForm, GoogleForm, NutritionForm, FoodNutrientsForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .API.YelpAPI.yelp import yelp_main, query_api
from .API.MapsAPI.maps import googlecode
from .API.SanjayAPI.nutrinix import nutritioncode
from .API.RobleAPI.nutrition import foodnutritioncode
from django.views.decorators.csrf import csrf_exempt
from .models import Business, Googlemodel, Nutritionmodel, Foodnutritionmodel

def index(request):
    return render(request,'app/index.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Application description page.',
            'year':datetime.now().year,
        }
    )

def foodie(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/foodie.html',
        {
            'title':'Foodie Page',
            'year':datetime.now().year,
        }
    )

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'app/login.html', {})

@csrf_exempt
def yelping(request):
    
    form = YelpForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        term = request.POST['term']
        location = request.POST['location']
        form.save()
        yelp_main(request)
        if request.GET.get('OK') == 'OK':
            messages.success(request, "Search successful." )
            return redirect('yelping')
            #return render(request, 'app/yelp.html', {'form' : form})
        else:    
            messages.error(request, "Unsuccessful Search. Invalid information.")

        assert isinstance(request, HttpRequest)
        
        yelp_data = Business.objects.all().order_by('-id').first()
        dic = {
            'yelp_data': yelp_data,
            }
        print(dic)
    
        return render(request, 'app/yelp.html', dic)
    return render(request, 'app/yelp.html', {
            'title':'Yelping',
            'year':datetime.now().year,
        })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("app:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="app/registration.html", context={"register_form":form})

@csrf_exempt
def googling(request):
    
    form = GoogleForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        Foodinput = request.POST['Foodinput']
        form.save()
        googlecode(Foodinput)
        if request.GET.get('OK') == 'OK':
            messages.success(request, "Search successful." )
            return redirect('googling')
            #return render(request, 'app/googleresults.html', {'form' : form})
        else:    
            messages.error(request, "Unsuccessful Search. Invalid information.")

        assert isinstance(request, HttpRequest)
        
        google_data = Googlemodel.objects.all().order_by('-id')
        dic = {
            'google_data': google_data,
        }
    
        return render(request, 'app/googleresults.html', dic)
    return render(request, 'app/googleresults.html', {
            'title':'Googling',
            'year':datetime.now().year,
     })

@csrf_exempt
def nutritioning(request):
    
    form = NutritionForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        Nutritioninput = request.POST['Nutritioninput']
        form.save()
        nutritioncode(Nutritioninput)
        if request.GET.get('OK') == 'OK':
            messages.success(request, "Search successful." )
            return redirect('nutritioning')
            #return render(request, 'app/googleresults.html', {'form' : form})
        else:    
            messages.error(request, "Unsuccessful Search. Invalid information.")

        assert isinstance(request, HttpRequest)
        
        nutrition_data = Nutritionmodel.objects.all().order_by('-id').first()
        dic = {
            'nutrition_data': nutrition_data,
        }
    
        return render(request, 'app/nutritionix.html', dic)
    return render(request, 'app/nutritionix.html', {
            'title':'Nutritioning',
            'year':datetime.now().year,
     })
@csrf_exempt
def foodmacros(request):
    
    form = FoodNutrientsForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        Macroinput = request.POST['Macroinput']
        form.save()
        foodnutritioncode(Macroinput)
        if request.GET.get('OK') == 'OK':
            messages.success(request, "Search successful." )
            return redirect('foodmacros')
           
        else:    
            messages.error(request, "Unsuccessful Search. Invalid information.")

        assert isinstance(request, HttpRequest)
        
        foodnutrition_data = Foodnutritionmodel.objects.all().order_by('-id').first()
        dic = {
            'foodnutrition_data': foodnutrition_data,
        }
    
        return render(request, 'app/foodnutrients.html', dic)
    return render(request, 'app/foodnutrients.html', {
            'title':'Foodmacros',
            'year':datetime.now().year,
     })
     