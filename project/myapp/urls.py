from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catagory/products/register/', views.Products_view, name= 'register'),
    path('catagory/', views.catagories, name='catagory'),

]