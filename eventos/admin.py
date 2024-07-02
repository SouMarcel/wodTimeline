# eventos/admin.py

from django.contrib import admin
from .models import Evento, Tempo

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug' ,'tempo')
    search_fields = ('nome', 'resumo', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}  # Define o campo slug baseado no campo nome

@admin.register(Tempo)
class TempoAdmin(admin.ModelAdmin):
    list_display = ('era', 'ano_ini', 'p_ini', 'ano_fim', 'p_fim', 'descricao' )
