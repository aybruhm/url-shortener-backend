# Django Imports
from django.urls import path

# Own Imports
from link.views import ShortenURL


app_name = "shortener"

urlpatterns = [
    path("shorten/", ShortenURL.as_view(), name="shorten-url"),
]
