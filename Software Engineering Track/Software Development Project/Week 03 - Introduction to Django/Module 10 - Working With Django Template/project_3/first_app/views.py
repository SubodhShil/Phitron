from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    details = {"author": 'Subodh', 'Age': 20}
    return render(request, 'home.html', details)