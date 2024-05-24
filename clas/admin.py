from django.contrib import admin
from .models import Disciplina, Cla

# Registra o modelo de Consulta da tabela completa
admin.site.register(Cla)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nivel', 'disciplina', 'descricao_preview', 'sistema_preview', 'efeito', 'livro', 'criado_em', 'atualizado_em')
    
    # Método para exibir uma prévia do campo 'descricao'
    def descricao_preview(self, obj):
        return obj.descricao[:30] + '...' if obj.descricao and len(obj.descricao) > 75 else obj.descricao
    # Define o nome da coluna que aparecerá na interface do Django Admin
    descricao_preview.short_description = 'descricao'
    
    # Método para exibir uma prévia do campo 'sistema'
    def sistema_preview(self, obj):
        return obj.sistema[:30] + '...' if obj.sistema and len(obj.sistema) > 75 else obj.sistema
    # Define o nome da coluna que aparecerá na interface do Django Admin
    sistema_preview.short_description = 'sistema'
    
    list_filter = ['disciplina']
    
    search_fields = ['nome']  # Adiciona o campo 'nome' como um campo de pesquisa
