from django.urls import path
from . import views
urlpatterns = [
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/<int:pk>/', views.product_detail, name='product_detail'),
    path('api/products/create/', views.product_create, name='product_create'),
    path('api/products/update/<int:pk>/', views.product_update, name='product_update'),
    path('api/products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('api/category/', views.category_list, name='category_list'),
    path('api/category/<int:pk>/', views.category_detail, name='category_detail'),
    path('api/category/create/', views.category_create, name='category_create'),
    path('api/category/update/<int:pk>/', views.category_update, name='category_update'),
    path('api/category/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('api/stock/', views.stock_list, name='stock_list'),
    path('api/stock/<int:pk>/', views.stock_detail, name='stock_detail'),
    path('api/stock/create/', views.stock_create, name='stock_create'),
    path('api/stock/update/<int:pk>/', views.stock_update, name='stock_update'),
    path('api/stock/delete/<int:pk>/', views.stock_delete, name='stock_delete'),

    path('api/invoice/', views.invoice_list, name='invoice_list'),
    path('api/invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('api/invoice/create/', views.invoice_create, name='invoice_create'),
    path('api/invoice/update/<int:pk>/', views.invoice_update, name='invoice_update'),
    path('api/invoice/delete/<int:pk>/', views.invoice_delete, name='stock_delete'),
    # path('api/register', views.register_api, name='register'),
]

