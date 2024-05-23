from django.contrib import admin
from .models import Disciplina, Cla

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome', 'nivel')
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome',)

@admin.register(Cla)
class ClaAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome',)
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome',)
