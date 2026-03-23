from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hi, welcome back. long time no see.')
    return render(request,'index.html')

def info(request):
    return HttpResponse('Finally you are back.')

def about(request):
    return HttpResponse('This time we got this.')