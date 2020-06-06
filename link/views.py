from django.shortcuts import render
from .shortener import Shortener
from .models import URL


# Create your views here.
def home(request):
    original_url = request.POST.get('original-url')
    link = ""
    # print(original_url)
    if request.method == 'POST':
        if request.POST.get('original-url'):
            url = URL()
            url.original_url = request.POST.get('original-url')
            NewUrl = url.save()
            link = Shortener().shorten()
            url.short_url = link
            # NewUrl = url.short_url
            NewUrl = url.save(force_insert=True)
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
