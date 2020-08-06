from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .shortener import Shortener
from .models import URL


def home(request):
    original_url = request.POST.get('original-url')
    if request.method == 'POST':
        if request.POST.get('original-url'):
            url = URL()
            url.original_url = request.POST.get('original-url')
            link = Shortener().shorten()
            url.short_url = link
            url.save()
            return redirect('add')
        else:
            original_url = request.POST.get('original-url')
    context = {
        'original_url': original_url,
    }
    return render(request, 'link/home.html', context)


def add(request):
    link = URL.objects.filter().last()
    return render(request, 'link/add.html', {'link': link})


def stats(request):
    urls = URL.objects.all().order_by('-timestamp')
    return render(request, 'link/stats.html', {'urls': urls})


def token(request, token):
    try:
        original_url = URL.objects.filter(short_url=token)[0]
        original_url.visits += 1
    except IndexError:
        return render(request, 'link/404.html')
    return redirect(original_url.original_url)
