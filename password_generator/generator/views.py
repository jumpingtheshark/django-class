from django.shortcuts import render
from django.http import HttpResponse  # added
import random


# Create your views here.

def home(request):  # function added
    return HttpResponse("fuck you")


def password1(request):
    return render(request, 'generator/password1.html')


def password2(request):
    # https://www.geeksforgeeks.org/type-conversion-python/
    lchar = request.GET.get('len')

    '''
      <input type="checkbox" id="schars" name="schars">
    <input type="checkbox" id="useCaps" name="useCaps">
    '''
    # return HttpResponse (lchar)
    length = int(lchar)
    scars = request.GET.get('schars')
    useCaps = request.GET.get('useCaps')
    print(scars)

    p = ''
    chars = 'abcdefghijklmonpqrstuvwxyz'

    if useCaps is not None:
        chars = 'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKMLM'

    for x in range(length):
        p += random.choice(chars)

    numbers ='0123456789'

    for x in range(3):
        p+= random.choice(numbers)



    if scars is not None:
        l_scars= "!@#$%%"
        p+=random.choice(l_scars)

    return render(request, 'generator/password2.html', {'password': p})
