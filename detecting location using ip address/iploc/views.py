from django.http import HttpResponse
from django.shortcuts import render,redirect
import ipapi
 
def city(request):
    ip=ipapi.location(ip="182.71.142.105")
    city=ip['city']
    print(ip,city)
    if city=='Bengaluru':
        print(city)
        return HttpResponse('you are in bengaluru')
    
    elif city=='Chennai':
        print(city)
        return HttpResponse('you are in chennai')
    else:
        return HttpResponse("other city")


def home(request):
    return render(request, 'iploc/home.html')
"""
def chennai(request):
    return render(request, 'iploc/chennai.html')

def bengalore(request):
    return render(request, 'iploc/bengaluru.html')"""

