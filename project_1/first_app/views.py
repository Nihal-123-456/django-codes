from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(response):
    return HttpResponse("This is courses")

def about(response):
    return HttpResponse("This is about")

def first_app_home(response):
    return HttpResponse("This is first app")