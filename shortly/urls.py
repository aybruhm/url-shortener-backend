# Django Imports
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# Rest Framework Imports
from rest_framework import permissions

# DRF Yasg Imports``
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from link import views

schema_view = get_schema_view(
   openapi.Info(
      title="URL Shortener",
      default_version='v1',
      description="A url shortening service built with Python (Django and Django Rest Framework).",
      contact=openapi.Contact(email="israelvictory87@gmail.com"),
      license=openapi.License(name="CC0-1.0 license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   
   # backend path
   path('', views.home, name='home'),
   path('<str:shortened_url>/', views.redirect_shortened_url, name="redirect-shortened-url"),
   
   # api endpoints
   path("api/", include("link.urls")),
   
   # api documentation endpoints
   re_path(r'^generate_api_documentation(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)