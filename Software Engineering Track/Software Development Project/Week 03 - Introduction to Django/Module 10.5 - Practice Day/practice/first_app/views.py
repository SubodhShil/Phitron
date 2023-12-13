from django.shortcuts import render
import datetime


def home(request):
    myContext = {
        'numbers': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'currentTime': datetime.datetime.now(),
        'GTAVIRelease': '',
        'word': 'm o t h e r l a n d',
        'word2': 'F A T H E R L A N D',
        'countries': ['Bangladesh', 'India', 'UK', 'Australia', 'South Korea', 'Japan'],
        'techVerse': 'The future of software engineers adaptability',
    }

    return render(request, 'show.html', myContext)
