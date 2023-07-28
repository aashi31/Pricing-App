# pricing_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for the app go here...
    path('', views.homepage, name='homepage'),
    path('calculate_price/', views.calculate_price, name='calculate_price'),
]

