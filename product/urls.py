#imports
from django.urls import path
from . import views

#defines all the URL routes for the website with each path focusing on a specific url pattern
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
