# eventos/admin.py

from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo', 'criado_em', 'atualizado_em')
    list_filter = ('tempo', 'criado_em')
    search_fields = ('nome', 'resumo', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}  # Define o campo slug baseado no campo nome

