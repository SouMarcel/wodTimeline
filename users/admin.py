from django.contrib import admin
from .models import Edicao

@admin.register(Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome', 'criado_em', 'atualizado_em')
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome',)
