from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, 'index.html')

def about(response):
    return render(response, 'about.html')

def contact(response):
    return render(response, 'contact.html')

def blog(response):
    return render(response, 'blog.html')

