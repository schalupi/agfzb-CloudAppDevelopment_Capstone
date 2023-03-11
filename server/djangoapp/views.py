from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'djangoapp/index.html')

# Create an `about` view to render a static about page
def about_us(request):
    return render(request, 'djangoapp/about_us.html')


# Create a `contact` view to return a static contact page
def contact_us(request):
    return render(request, 'djangoapp/contact_us.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    return render(request, 'djangoapp/login.html')

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            return render(request, 'djangoapp/login.html', {'error': 'Invalid username or password.'}, context)
    else:
        return render(request, 'djangoapp/login.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_view(request):
    logout(request)
    return redirect('djangoapp:index')


# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

def registration_view(request):
    if request.method == 'POST':
        # Extract user information from request.POST
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            context = {'error_message': 'User already exists!'}
            return render(request, 'djangoapp/registration.html', context)
        # If not, create a new user
        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, password=password)
        # Log in the user and redirect to index page
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('djangoapp:index')
    else:
        return render(request, 'djangoapp/registration.html')




# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

