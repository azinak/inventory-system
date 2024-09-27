
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/add', views.add_product, name='add_product'),
    path('products/delete', views.delete_product, name='delete_product'),
    path('products/update', views.update_product, name='update_product'),
]
