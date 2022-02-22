from django.shortcuts import render
from django.http import HttpResponse #added

# Create your views here.

def home (request): #function added
    return  HttpResponse("fuck you")
