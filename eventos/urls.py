# eventos/urls.py

from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('detalhe/<int:pk>/', views.detalhe, name='detalhe'),
    path('novo/', views.novo, name='novo'),
    path('edit_delete/<int:pk>/', views.edit_delete, name='edit_delete'),
]
