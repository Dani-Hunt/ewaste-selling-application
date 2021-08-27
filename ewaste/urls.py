from typing import ValuesView
from django.urls import path
from . import views
from .views import (
LaptopsDetailView,
PhonesCreateView,
PhonesDeleteView,
PhonesDetailView, 
PhonesUpdateView, 
LaptopsCreateView, 
LaptopsUpdateView, 
LaptopsDeleteView, 
OthersDetailView,
OthersCreateView, 
OthersDeleteView, 
OthersUpdateView, cart, others
)


urlpatterns = [
    path('', views.home, name="ewaste-home"),
    path('phones/<int:pk>/', PhonesDetailView.as_view(), name="phones-detail"),
    path('laptops/<int:pk>/', LaptopsDetailView.as_view(), name="laptops-detail"),
    path('others/<int:pk>/', OthersDetailView.as_view(), name="others-detail"),
    path('about/', views.about, name="ewaste-about"),
    path('desktops/', views.desktops, name="ewaste-desktops"),
    path('phones/', views.phones, name="ewaste-phones"),
    path('laptops/', views.laptops, name="ewaste-laptops"),
    path('others/', views.others, name="ewaste-others"),
    path('update_item/', views.updateItem, name="update_item"),
    path('cart/', views.cart, name="cart"),

    path('phones/new/', PhonesCreateView.as_view(), name='phones-create'),
    path('phones/<int:pk>/update', PhonesUpdateView.as_view(), name="phones-update"),
    path('phones/<int:pk>/delete', PhonesDeleteView.as_view(), name="phones-delete"),

    path('laptops/new/', LaptopsCreateView.as_view(), name='laptops-create'),
    path('laptops/<int:pk>/update',
         LaptopsUpdateView.as_view(), name="laptops-update"),
    path('laptops/<int:pk>/delete',
         LaptopsDeleteView.as_view(), name="laptops-delete"),

    path('others/new/', OthersCreateView.as_view(), name='others-create'),
    path('others/<int:pk>/update',
         OthersUpdateView.as_view(), name="others-update"),
    path('others/<int:pk>/delete',
         OthersDeleteView.as_view(), name="others-delete"),

]
