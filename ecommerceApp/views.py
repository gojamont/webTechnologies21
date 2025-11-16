from django.shortcuts import render,redirect
from .models import Product, User
from django.contrib.auth import authenticate, login
import json


# Create your views here.

# index page
def index(request):
    return render(request, "home.html");

def about(request):
    return render(request, "AboutPage.html");

# function for authenticating the user
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return render(request, "loginPage.html", {'error':'Username or password is required'})
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "loginPage.html", {'error':'Invalid credentials'})
        except json.JSONDecodeError:
                return render(request, "loginPage.html", {'error':'Invalid request'})
        except Exception as error:
                return render(request, "loginPage.html", {'error':'Error occurred while trying to login a user, please try again'})
    return render(request, "loginPage.html")

def promoCodePage(request):
    return render(request, "promoCodePage.html");

# function for registering the user
def register(request):
    if request.method == "POST":
        try:
            # getting all the data from the frontend
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            
            user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            return redirect("register")
        except Exception as error:
            return render(request, "registerPage.html", {'error':'Error occurred while trying to register, please try again'})
            
    return render(request, "registerPage.html");

def catalogPage(request):
    products = Product.objects.all()
    return render(request, "CatalogPage.html", {'products': products})

def productPage(request, productId):
    product = Product.objects.get(id=productId)
    return render(request, "ProductPage.html", {'product': product})

def cartPage(request):
    return render(request, "CartPage.html");