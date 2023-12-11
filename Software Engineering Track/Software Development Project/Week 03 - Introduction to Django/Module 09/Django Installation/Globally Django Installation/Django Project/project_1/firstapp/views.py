from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("This is firstapp home page")

def aboutPage(request):
    return HttpResponse("This is firstapp about page")

def courses(request):
    return HttpResponse("This is course page.")
