from django import forms
from .models import Personagem
from disciplinas.models import Disciplina

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = (
            'nome', 'alcunha', 'mote', 'biografia', 'ficha_url', 'ficha_pdf', 'nascimento', 'abraco',
            'morte_final', 'geracao', 'senhor', 'cla', 'disciplinas', 'livro'
        )
        
        widgets = {
            'disciplinas': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(PersonagemForm, self).__init__(*args, **kwargs)
        # Filtra as disciplinas para mostrar apenas aquelas com nível diferente de zero
        self.fields['disciplinas'].queryset = Disciplina.nivel_nzero()