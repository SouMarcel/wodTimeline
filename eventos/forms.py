# eventos/forms.py

from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'local', 'livro', 'personagem', 'resumo', 'descricao', 'tempo']
