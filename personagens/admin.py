from django.contrib import admin
from .models import Personagem

class PersonagemAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'alcunha', 'mote_preview', 'biografia_preview', 'ficha',
        'nascimento', 'idade', 'abraco', 'morte_final', 'geracao', 
        'senhor', 'cla', 'disciplinas_list', 'livro'
    )

    def disciplinas_list(self, obj):
        return ", ".join([disciplina.nome for disciplina in obj.disciplinas.all()])
    disciplinas_list.short_description = 'Disciplinas'

    def mote_preview(self, obj):
        return obj.mote[:75] + '...' if obj.mote and len(obj.mote) > 75 else obj.mote
    mote_preview.short_description = 'Mote'

    def biografia_preview(self, obj):
        return obj.biografia[:75] + '...' if obj.biografia and len(obj.biografia) > 75 else obj.biografia
    biografia_preview.short_description = 'Biografia'

    filter_horizontal = ('disciplinas',)

admin.site.register(Personagem, PersonagemAdmin)
