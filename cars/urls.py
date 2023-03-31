from django import views
from django.urls import path
from cars import views

urlpatterns = [
    path('',views.cars, name="cars")
]