# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'map', views.map, name='map'),
    url(r'phone', views.phone, name='phone'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

