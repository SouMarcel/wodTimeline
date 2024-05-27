# livros/forms.py

from django import forms
from .models import Livro, Edicao

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'edicao', 'editora', 'revisao', 'isbn']

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['nome']
