from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello Boi meets world....')

def about(repsonse):
    return HttpResponse("About Boi meets World!!")

def  contact(response):
    return HttpResponse("Contact boi meets World")

def blog(response):
    return HttpResponse("Blog about boi meets world")

