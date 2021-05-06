from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/custom_products/',
         views.custom_products, name='custom_products'),
    path('fabric/<int:fabric_id>/', views.fabric_detail, name='fabric_detail'),
    path('add/', views.add_product, name='add_product'),
]