from . import views
from django.urls import path

urlpatterns = [
    path('', views.front, name='front'),
    path(r'services/', views.services, name='about'),
    path(r'contact/', views.contact, name='contact'),
]