from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('employee/', views.Employee, name="employee"),
    path('add-employee/', views.AddEmployee, name="add-employee"),
]
