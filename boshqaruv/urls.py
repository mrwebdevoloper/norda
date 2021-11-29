from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('clients/', Client),
    path('shop/', Shops),
    path('qabul/', Qabulqil),
    path('qaytarilgan/', Qaytar),
    path('buyurtmaolinyapti/', Buyurtma),
    path('shopitem/<int:pk>/', Shopitem),
    path('buyurtmaqabul/<int:pk>/', Qabul),
    path('ochirsh/<int:pk>/', Ochirish),
    
]