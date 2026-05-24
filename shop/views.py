from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Welcome to homepage")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')