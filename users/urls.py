from django.urls import path
from . import views

# Definição das rotas para o app 'users'
urlpatterns = [
    path('login/', views.login_view, name='login'),  # Rota para a página de login
    path('logout/', views.logout_view, name='logout'),  # Rota para a página de logout
    path('register/', views.register_view, name='register'),  # Rota para a página de registro
]
