from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/<int:pk>/', views.product_detail, name='product_detail'),
    path('api/products/create/', views.product_create, name='product_create'),
    path('api/products/update/<int:pk>/', views.product_update, name='product_update'),
    path('api/products/delete/<int:pk>/', views.product_delete, name='product_delete')
]