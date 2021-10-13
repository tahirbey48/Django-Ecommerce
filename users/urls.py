from django.contrib import admin
from django.urls import path
from . import views
app_name = "users"

urlpatterns = [
    path('login/',views.loginfun, name = "login"),
    path('logout/',views.logoutfun, name = "logout"),
    path('register/',views.registerfun, name = "register"),
]