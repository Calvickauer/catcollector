from django.shortcuts import render
from django.http import HttpResponse

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    
    def __str__(self):
        return f"{self.name}"


cats = [
    Cat("Jimmy", "Criqourtor", "Freaky with sauciness", 103),
    Cat("Billy", "Bildonic", "Gravy kitty", 2),
    Cat("Garfield", "Siamese", "Fat and mean", 10)
]

# Create your views here.
def index(response):
    return render(response, 'index.html', { 'cats': cats })

def about(response):
    return render(response, 'about.html')

def contact(response):
    return render(response, 'contact.html')

def blog(response):
    return render(response, 'blog.html')

