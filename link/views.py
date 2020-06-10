from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
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
            print(link)
            url.save()
            return redirect('add')
        else:
            original_url = request.POST.get('original-url')
    context = {
        'original_url': original_url,
        'link': link,
    }
    return render(request, 'home.html', context)


def add(request):
    link = URL.objects.filter().last()
    return render(request, 'add.html', {'link': link})


def stats(request):
    urls = URL.objects.all().order_by('-timestamp')
    print(urls)
    return render(request, 'stats.html', {'urls': urls})


def token(request, token):
    try:
        original_url = URL.objects.filter(short_url=token)[0]
        original_url.visits += 1
    except IndexError:
        return render(request, '404.html')
    return redirect(original_url.original_url)