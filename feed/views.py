from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return HttpResponse("<h1>Hi there again from chandresh</h1>")
