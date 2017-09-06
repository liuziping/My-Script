from django.http import HttpResponse
from django.shortcuts import render

def index(request):                 
    return HttpResponse('<h1>This is my first blog</h1>')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
    
def sum(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))
    
