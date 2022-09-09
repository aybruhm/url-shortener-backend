# Django Imports
from django.urls import path

# Own Imports
from link.views import (
    ShortenURL, 
    GetOriginalURl,
    URLStats
)

app_name = "shortener"

urlpatterns = [
    path("shorten/", ShortenURL.as_view(), name="shorten-url"),
    path("<str:token>/", GetOriginalURl.as_view(), name="shorten-url-token"),
    path("stats/", URLStats.as_view(), name="stats"),
]
