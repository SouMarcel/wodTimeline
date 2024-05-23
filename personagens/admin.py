from django.contrib import admin
from .models import Personagem

# Definindo uma classe admin personalizada para o modelo Personagem
class PersonagemAdmin(admin.ModelAdmin):
    # Especifica os campos que serão exibidos na lista de visualização do Django Admin
    list_display = (
        'nome', 'alcunha', 'mote_preview', 'biografia_preview', 'ficha',
        'nascimento', 'idade', 'abraco', 'morte_final', 'geracao', 
        'senhor', 'cla', 'disciplinas_list', 'livro'
    )

    # Método para exibir a lista de disciplinas associadas a um personagem
    def disciplinas_list(self, obj):
        # Junta os nomes das disciplinas em uma única string, separadas por vírgula
        return ", ".join([disciplina.nome for disciplina in obj.disciplinas.all()])
    # Define o nome da coluna que aparecerá na interface do Django Admin
    disciplinas_list.short_description = 'Disciplinas'

    # Método para exibir uma prévia do campo 'mote'
    def mote_preview(self, obj):
        # Retorna os primeiros 75 caracteres do mote, seguidos por "..." se for maior que 75 caracteres
        return obj.mote[:75] + '...' if obj.mote and len(obj.mote) > 75 else obj.mote
    # Define o nome da coluna que aparecerá na interface do Django Admin
    mote_preview.short_description = 'Mote'

    # Método para exibir uma prévia do campo 'biografia'
    def biografia_preview(self, obj):
        # Retorna os primeiros 75 caracteres da biografia, seguidos por "..." se for maior que 75 caracteres
        return obj.biografia[:75] + '...' if obj.biografia and len(obj.biografia) > 75 else obj.biografia
    # Define o nome da coluna que aparecerá na interface do Django Admin
    biografia_preview.short_description = 'Biografia'

    # Adiciona a funcionalidade de seleção múltipla para o campo 'disciplinas' na interface do Django Admin
    filter_horizontal = ('disciplinas',)

# Registra o modelo Personagem e a classe PersonagemAdmin no Django Admin
admin.site.register(Personagem, PersonagemAdmin)
