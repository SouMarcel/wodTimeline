from django import forms
from .models import Cla
from disciplinas.models import Disciplina


class ClaForm(forms.ModelForm):
    
    class Meta:
        model = Cla
        fields = [
            'nome', 'historia', 'apelido', 'mote', 'seita', 'aparencia', 'refugio',
            'cria_persona', 'fraquezas', 'organizacao', 'antecedentes', 'estereotipos',
            'logo', 'disciplinas', 'livro',
        ]
    # O método __init__ é chamado ao criar uma instância do formulário
    def __init__(self, *args, **kwargs):
        super(ClaForm, self).__init__(*args, **kwargs)
        # Filtra as disciplinas para mostrar apenas aquelas com nível 0 no proprio formulario
        # self.fields['disciplinas'].queryset = Disciplina.objects.filter(nivel=0) 
        # Filtra as disciplinas para mostrar apenas aquelas com nível 0 usando models importado
        self.fields['disciplinas'].queryset = Disciplina.nivel_zero()