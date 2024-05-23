from django.contrib import admin
from .models import Personagem

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome', 'alcunha', 'nascimento', 'cla', 'criado_em', 'atualizado_em')
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome', 'alcunha')
    # Filtros disponíveis na interface de administração para filtrar os registros por clã
    list_filter = ('cla',)

