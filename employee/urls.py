from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('employee/', views.Employee, name="employee"),
    path('add-employee/', views.AddEmployee, name="add-employee"),
    path('employee-profile/<int:pk>/', views.EmployeeProfile, name="employee-profile"),
    path('return-device/<int:pk>/', views.ReturnDevice, name="return-device"),
]
