"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('catalog', views.catalogPage, name="catalog"),
    path('products/add/', views.add_product, name='add_product'),
    path('catalog/<int:productId>', views.productPage, name="product"),
    path('catalog/<int:productId>/edit', views.editProductPage, name="product_editor"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('cart', views.cartPage, name="cart")
]