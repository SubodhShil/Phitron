from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    details = {"author": 'Subodh', 'Age': 24, 'list': ['1', '2', '3'], 'birthday': datetime.datetime.now(),  'test': '', 'courses': [
        {
            'id': 1,
            'name': 'DSA',
            "fee": 10000
        },
        {
            "id": 2,
            'name': 'MERN Stack',
            "fee": 12000
        },
        {
            "id": 3,
            'name': 'N4 Course',
            "fee": 15000
        },
        {
            "id": 4,
            "name": 'Behavioural course',
            "fee": 20000
        }
    ]}

    return render(request, 'first_app/home.html', details)
