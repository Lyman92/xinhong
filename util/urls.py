from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path(r'^(?P<method>\w*)/$', views.index, name='index'),
    path('setFlash/', views.setFlash, name='setFlash'),
    url(r'^(?P<method>\w*)/*$', views.index, name='index'),
]
