from django.contrib import admin
from django.urls import path, include
from account_app import views

urlpatterns = [
    path('login/', views.sign_in),
    path('signout/', views.sign_out),
    path('register/', views.register),
]
