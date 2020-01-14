from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contact import views

urlpatterns = [
   path('index',views.index,name="index")
]