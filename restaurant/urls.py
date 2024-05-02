"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_app.views import index, restaurants, restaurant_detail, dishes, dish_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('restaurants/', restaurants, name="restaurants"),
    path('restaurant_details/<int:restaurant_id>/', restaurant_detail, name="restaurant details"),
    path('dishes/', dishes, name="dishes"),
    path('dish_deteils/<int:dish_id>', dish_detail, name="Dish details")

]
