
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/add', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
