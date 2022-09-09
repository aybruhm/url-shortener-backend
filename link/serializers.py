# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from link.models import URL


class URLSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = URL
        fields = ["original_url"]