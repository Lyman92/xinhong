from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='main_welcome'),
    path('index/', views.index, name='main_index'),
    path('contact_us/', views.contact_us, name='main_contact_us'),
]
