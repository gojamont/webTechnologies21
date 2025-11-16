from django.shortcuts import render,redirect
from .models import Product, User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

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
                return JsonResponse({'success': True, 'message':'User logged in successfully'})
            else:
                return JsonResponse({'success': False, 'message':'Invalid credentials'})
        except json.JSONDecodeError:
                return JsonResponse({'success': False, 'message':'Invalid request'})
        except Exception as error:
                return JsonResponse({'success': False, 'message':f'An error occurred:{error}'})
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
            
            # error handling
            if not username or not password or not email:
                return JsonResponse({'success': False, 'message':'Username, password or email does not exist'})
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success':False, 'message':'Username already exists'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success':False, 'message':'Email already exists'}, status=400)
            
            # saving user in the data base
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            
            return JsonResponse({'success':True, 'message':'User is registered successfully'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid data'}, status=400)
            
        except Exception as error:
            return JsonResponse({'success':False, 'message': f'An error occurred: {error}'},  status=500)
            
    return render(request, "registerPage.html");

def logout_view(request):
    logout(request)
    return redirect('/')

def catalogPage(request):
    products = Product.objects.all()
    return render(request, "CatalogPage.html", {'products': products})

def productPage(request, productId):
    product = Product.objects.get(id=productId)
    return render(request, "ProductPage.html", {'product': product})

def cartPage(request):
    return render(request, "CartPage.html");