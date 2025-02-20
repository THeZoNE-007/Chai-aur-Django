# from django.contrib import admin
from django.urls import path
from . import views 

# We are keeping the views above since we have the file called views here as there was one in project folder

# localhost:8000/chai --> '' i.e. this has become the home in this app

# localhost:8000/chai/order --> order/ i.e. these will be the pages/functions other that home (only if there are more pages)

urlpatterns = [
    path('',views.all_chai, name='all_chai'),
]