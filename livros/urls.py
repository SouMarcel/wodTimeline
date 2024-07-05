# livros/urls.py

from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.home, name="home"),
    path('lista/', views.livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livro_novo/', views.livro_create, name='livro_create'),
    path('edicao/', views.edicao_list, name='edicao_list'),
    path('edicao/<int:pk>/', views.edicao_detail, name='edicao_detail'),
    path('edicao_nova/', views.edicao_create, name='edicao_create'),
]
