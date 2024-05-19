from django.contrib import admin
from django.urls import path, include

# Definição das rotas principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a área administrativa
    path('users/', include('users.urls')),  # Inclusão das rotas do app 'users'
]
