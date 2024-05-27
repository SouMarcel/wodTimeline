# admin.py

from django.contrib import admin
from .models import Edicao, Livro

class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em', 'atualizado_em')
    search_fields = ('nome',)

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'edicao', 'editora', 'revisao', 'isbn', 'criado_em', 'atualizado_em')
    list_filter = ('edicao', 'editora')
    search_fields = ('nome', 'editora', 'isbn')

# Registro dos modelos no admin com personalização
admin.site.register(Edicao, EdicaoAdmin)
admin.site.register(Livro, LivroAdmin)
