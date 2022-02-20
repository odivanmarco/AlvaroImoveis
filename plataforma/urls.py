from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('financiamento', views.financiamento, name='financiamento'),
    path('faleconosco', views.faleconosco, name='faleconosco'),
   path('imovel/<str:id>', views.imovel, name="imovel"),
]