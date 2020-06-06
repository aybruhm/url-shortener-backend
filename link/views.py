from django.shortcuts import render
from .shortener import Shortener
from .models import URL


# Create your views here.
def home(request):
    original_url = request.POST.get('original-url')
    link = ""
    print(original_url)
    if request.method == 'POST':
        if request.POST['original-url']:
            NewUrl = original_url#.save(commit=False)
            print(NewUrl)
            link = Shortener().shorten()
            NewUrl.short_url = link
            NewUrl#.save()
        else:
            original_url = request.POST.get('original-url')

    context = {
        'original_url': original_url,
    }
    return render(request, 'home.html', context)


def add(request):
    return render(request, 'add.html')


def token(request):
    pass


def stats(request):
    return render(request, 'stats.html')
