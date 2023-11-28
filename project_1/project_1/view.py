from django.http import HttpResponse

def contact(response):
    return HttpResponse("This is contact page")

def home(response):
    return HttpResponse("This is home page")