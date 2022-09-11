# Django Imports
from django.urls import path

# Own Imports
from link.views import (
    ShortenURLAPIView, 
    GetOriginalURLAPIView,
    URLStatsAPIView
)

app_name = "shortener"

urlpatterns = [
    path("shorten/", ShortenURLAPIView.as_view(), name="shorten-url"),
    path("<str:token>/", GetOriginalURLAPIView.as_view(), name="shorten-url-token"),
    path("stats/", URLStatsAPIView.as_view(), name="stats"),
]
