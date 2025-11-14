from django.shortcuts import render
from .models import Product

# Create your views here.

# index page
def index(request):
    return render(request, "home.html");

def about(request):
    return render(request, "AboutPage.html");

def login(request):
    return render(request, "loginPage.html");

def promoCodePage(request):
    return render(request, "promoCodePage.html");

def register(request):
    return render(request, "registerPage.html");

def catalogPage(request):
    products = Product.objects.all()
    return render(request, "CatalogPage.html", {'products': products})

def cartPage(request):
    return render(request, "CartPage.html");