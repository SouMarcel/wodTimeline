from django.contrib import admin
from .models import Livro, Personagem

class LivroAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos no formulário de administração
    fields = ('nome', 'edicao', 'editora', 'revisao', 'isbn')

    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome', 'edicao', 'editora', 'revisao', 'isbn', 'criado_em', 'atualizado_em')
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome', 'editora', 'isbn')

# Registrar o modelo Livro com a configuração personalizada do admin
admin.site.register(Livro, LivroAdmin)

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    # Lista de campos a serem exibidos na interface de administração
    list_display = ('nome', 'alcunha', 'nascimento', 'cla', 'criado_em', 'atualizado_em')
    # Campos de pesquisa para facilitar a localização de registros na interface de administração
    search_fields = ('nome', 'alcunha')
    # Filtros disponíveis na interface de administração para filtrar os registros por clã
    list_filter = ('cla',)
