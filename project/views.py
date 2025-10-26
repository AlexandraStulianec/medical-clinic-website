from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def cardiology(request):
    return render(request, 'cardiology.html')

def dentistry(request):
    return render(request, 'dentistry.html')

def psychiatry(request):
    return render(request, 'psychiatry.html')

