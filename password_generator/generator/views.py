from django.shortcuts import render
from django.http import HttpResponse #added
import random

# Create your views here.

def home (request): #function added
    return  HttpResponse("fuck you")
    

def password1 (request):
    return render (request, 'generator/password1.html')


def password2 (request):
    # https://www.geeksforgeeks.org/type-conversion-python/
    lchar=request.GET.get('len')
    #return HttpResponse (lchar)
    length=int(lchar)
    p=''
    chars = 'abcdefghijklmonpqrstuvwxyz'
    for x in range (length):
        p+= random.choice(chars)


    
    return render (request, 'generator/password2.html', {'password':p})
