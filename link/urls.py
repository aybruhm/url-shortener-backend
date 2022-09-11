# Django Imports
from django.urls import path

# Own Imports
from link.views import (
    ShortenURLAPIView, 
    URLStatsAPIView
)

app_name = "shortener"

urlpatterns = [
    path("shorten/", ShortenURLAPIView.as_view(), name="shorten-url"),
    path("stats/", URLStatsAPIView.as_view(), name="stats"),
]
