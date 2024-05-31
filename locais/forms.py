from django import forms 
from .models import Local

# Formalario
class LocalForm(forms.ModelForm):
    
    class Meta:
        model = Local
        fields = (
            'nome', 'regiao', 'dimensao', 'era', 'livro'
        )
