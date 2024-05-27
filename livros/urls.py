# livros/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('novo/', views.livro_create, name='livro_create'),
]
