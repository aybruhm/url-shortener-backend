# Rest Framework Imports
from rest_framework import serializers

# Django Imports
from django.contrib.sites.shortcuts import get_current_site

# Own Imports
from link.models import URL


class ShortenURLSerializer(serializers.Serializer):
    original_url = serializers.URLField(required=True)
    

class URLSerializer(serializers.ModelSerializer):
    
    visits = serializers.SerializerMethodField(read_only=True)
    short_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = URL
        fields = ("original_url", "short_url", "visits", "timestamp")
        
    def get_visits(self, value):
        """
        It takes a short url and returns the number of visits to that url
        
        :param value: The value of the URL that the user entered
        :return: The number of visits to the short URL.
        """
        url = URL.objects.get(short_url=value)
        visits = int(url.visits)
        return visits
    
    def get_short_url(self, value):
        """
        If the value is not empty, then return the current site's domain and the value. Otherwise,
        return an empty string
        
        :param value: The value of the field that we are serializing
        :return: The domain of the current site and the value.
        """

        request = self.context.get("request")
        current_site = get_current_site(request)
        
        if value:
            value = current_site.domain + f"/{value}/"
        else:
            value = ""
            
        return value