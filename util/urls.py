from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/edit/', views.edit_product, name='edit_product'),
    path('products/edit_content/', views.edit_product_content, name='edit_product_content'),
    path('get_uptoken/', views.get_uptoken, name='get_uptoken'),
]
