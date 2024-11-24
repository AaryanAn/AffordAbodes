from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Local products
    path('external/', views.house_listings, name='house_listings'),  # API properties
]