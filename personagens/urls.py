from django.urls import path
from .views import PersonagemDetailView

urlpatterns = [
    path('personagem/<int:pk>/', PersonagemDetailView.as_view(), name='Personagem_detail'),
]
