from django.shortcuts import render, redirect
from django.http import HttpResponse
from .shortener import Shortener
from .models import URL



def home(request):
    original_url = request.POST.get('original-url')
    link = ""
    if request.method == 'POST':
        if request.POST.get('original-url'):
            url = URL()
            url.original_url = request.POST.get('original-url')
            link = Shortener().shorten()
            url.short_url = link
            url.save()
        else:
            original_url = request.POST.get('original-url')

    context = {
        'original_url': original_url,
        'link': link,
    }
    return render(request, 'home.html', context)


def add(request):
    return render(request, 'add.html')


def token(request, token):
    try:
        original_url = URL.objects.filter(short_url=token)[0]
        original_url.visits += 1
    except IndexError:
        return render(request, '404.html')
    return redirect(original_url.original_url)


def stats(request):
    urls = URL.objects.all()
    return render(request, 'stats.html', {'urls': urls})