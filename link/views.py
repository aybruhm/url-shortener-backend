# Django Imports
from django.shortcuts import render, redirect
from django.db.models import F

from .shortener import Shortener

# Native Imports
from string import ascii_letters, digits
from random import choices

# Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# YASG Imports
from drf_yasg.utils import swagger_auto_schema

# Own Imports
from link.models import URL
from link.serializers import URLSerializer, ShortenURLSerializer

# Third Libraries Imports
from rest_api_payload import success_response, error_response


class ShortenURL(APIView):
    short_url_serializer_class = ShortenURLSerializer
    serializer_class = URLSerializer
    no_of_characters = 5
    
    def shorten_url(self):
        shrtn_url =  ''.join(
            choices(
                ascii_letters+digits*2, 
                k=self.no_of_characters
            )
        )
        return shrtn_url
    
    @swagger_auto_schema(request_body=short_url_serializer_class)
    def post(self, request:Request) -> Response:
        serializer = self.short_url_serializer_class(data=request.data)
        
        if serializer.is_valid():
            original_url = serializer.validated_data.get("original_url")
            
            # get url or create one
            url, _ = URL.objects.get_or_create(original_url=original_url)
            # shortens original url to short_url
            url.short_url = self.shorten_url()
            # save url object
            url.save()
            
            payload = success_response(
                status=True, 
                message="Url shortended!",
                data=self.serializer_class(url).data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        
        payload = error_response(
            status=False,
            message=serializer.errors
        )
        return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
    

class GetOriginalURl(APIView):
    
    def get(self, request:Request, token:str) -> Response:
        
        try:
            url = URL.objects.filter(short_url=token).first()
            url.visits = F("visits") + 1
            url.save()
        except (URL.DoesNotExist, Exception):
            payload = error_response(
                status=False,
                message="URL does not exist!"
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        
        payload = success_response(
            status=True,
            message="URL retrieved!",
            data={}
        )
        return Response(data=payload, status=status.HTTP_200_OK)


