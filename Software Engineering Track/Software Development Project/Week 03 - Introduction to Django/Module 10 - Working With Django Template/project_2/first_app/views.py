from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("I am something")
    return render(request, "first_app/home.html")
