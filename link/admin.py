# Django Imports
from django.contrib import admin

# Own Imports
from link.models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = [
        "original_url", "short_url", "visits", "timestamp"
    ]