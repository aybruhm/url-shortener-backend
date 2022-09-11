# Django Imports
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import F

# Native Imports
from string import ascii_letters, digits
from random import choices

# Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

# YASG Imports
from drf_yasg.utils import swagger_auto_schema

# Own Imports
from link.models import URL
from link.serializers import URLSerializer, ShortenURLSerializer

# Third Libraries Imports
from rest_api_payload import success_response, error_response


def shortly_backend_home(request:HttpRequest) -> HttpResponse:
    return render(request, "shortener/home.html")


def redirect_shortened_url(request:HttpRequest, shortened_url:str) -> HttpResponseRedirect:
    """
    It takes a request and a shortened URL, and returns a redirect to the original URL
    
    :param request: This is the request object that is passed to the view
    :type request: HttpRequest
    :param shortened_url: The shortened URL that was passed in the URL
    :type shortened_url: str
    :return: HttpResponseRedirect
    """
    
    try:
        url = URL.objects.filter(short_url=shortened_url).first()
        url.visits = F("visits") + 1
        url.save()
    except (URL.DoesNotExist, Exception):
        raise Http404
    
    return HttpResponseRedirect(redirect_to=url.original_url)


class ShortenURLAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    short_url_serializer_class = ShortenURLSerializer
    serializer_class = URLSerializer
    no_of_characters = 5
    
    def shorten_url(self):
        """
        It returns a string of random characters of length no_of_characters
        :return: A string of random characters.
        """
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
                data=self.serializer_class(url, context={'request': request}).data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        
        payload = error_response(
            status=False,
            message=serializer.errors
        )
        return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
    

class URLStatsAPIView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = URLSerializer
    
    def get(self, request:Request) -> Response:
        """
        This APIView gets all the URLs from the database and returns them in a JSON response
        
        :param request: This is the request object that is sent to the view
        :type request: Request
        :return: A list of URLs
        """
        urls = URL.objects.all()
        serializer = self.serializer_class(urls, many=True, context={'request': request})
        
        payload = success_response(
            status=True, 
            message="URLs retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    