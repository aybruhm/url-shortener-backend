# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from link.models import URL


class ShortenURLSerializer(serializers.Serializer):
    original_url = serializers.URLField(required=True)
    

class URLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = URL
        fields = ("original_url", "short_url", "visits", "timestamp")
        