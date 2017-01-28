"""pwc_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/user/$', user_face_file_upload, name='user_face_file_upload'),
    url(r'^upload/picture/$', file_upload, name='file_upload'),
    url(r'^get/face_list/$', get_face_list, name='get_face_list'),
    url(r'^get/picture_list/$', get_picture_list, name='get_picture_list'),
    url(r'^get/similar_list/$', get_similar_list, name='get_similar_list'),
]