from django.contrib import admin
from django.urls import path, include
from . import views

# Definição das rotas principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a área administrativa
    path('clas/', include('clas.urls')),
    path('users/', include('users.urls')),  # Inclusão das rotas do app 'users'
    path('', views.index, name='index')
]
