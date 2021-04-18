# This file is copied from the Booutique Ado project.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout')
]