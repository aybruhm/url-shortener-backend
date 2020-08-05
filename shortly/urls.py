from django.contrib import admin
from django.urls import path
from link import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shorten-link/', views.add, name='add'),
    path('stats/', views.stats, name='stats'),
    path('<str:token>', views.token, name='token'),
]
