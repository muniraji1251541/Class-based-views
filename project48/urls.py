"""project48 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('fbv_string/',fbv_string,name='fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),

    path('fbv_htmlpage/',fbv_htmlpage,name='fbv_htmlpage'),
    path('Cbv_htmlpage/',Cbv_htmlpage.as_view(),name='Cbv_htmlpage'),

    path('fbv_djangoform/',fbv_djangoform,name='fbv_djangoform'),
    path('Cbv_djangoform/',Cbv_djangoform.as_view(),name='Cbv_djangoform'),

    path('fbv_modelform/',fbv_modelform,name='fbv_modelform'),
    path('display_profile/',display_profile,name='display_profile'),
    path('Cbv_modelform/',Cbv_modelform.as_view(),name='Cbv_modelform'),
]
