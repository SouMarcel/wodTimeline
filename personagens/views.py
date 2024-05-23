from django.views.generic import DetailView
from .models import Personagem

class PersonagemDetailView(DetailView):
    model = Personagem
    template_name = 'personagens/personagem_detail.html'
