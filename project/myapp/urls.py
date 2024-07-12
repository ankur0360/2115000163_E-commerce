from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catagory/products/register/', views.Products_view, name= 'register'),
    path('catagory/', views.catagories_items, name='catagory'),
    path('catagory/products/<int:pk>/', views.catagories, name='catagories_items')
]