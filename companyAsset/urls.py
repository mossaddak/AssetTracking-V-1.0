from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('add-asset/', views.AddAsset, name="add-asset"),
    path('delete-asset/<int:pk>/', views.DeleteAsset, name="delete-asset")
]
  