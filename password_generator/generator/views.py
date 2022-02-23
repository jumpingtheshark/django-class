from django.shortcuts import render
from django.http import HttpResponse #added

# Create your views here.

def home (request): #function added
    return  HttpResponse("fuck you")
    

def password1 (request):
    length=request.GET.get('length')
    #return render (request, 'generator/password.html', {'password':length})
    return render (request, 'generator/password1.html')


def password2 (request):
    length=request.GET.get('length')
    return render (request, 'generator/password2.html', {'password':length})
    #return HttpResponse('fuck you')