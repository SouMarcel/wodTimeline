
from django.contrib import admin
from .models import Disciplina


# Register your models here.
@admin.register(Disciplina) # é o mesmo codigo que admin.site.register(Disciplina, DisciplinaAdmin)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel', 'disciplina', 'descricao_preview',
                    'sistema_preview', 'efeito_preview', 'livro'
                    )
    
    # Método para exibir uma prévia do campo 'descricao'
    def descricao_preview(self, obj):
        return obj.descricao[:30] + '...' if obj.descricao and len(obj.descricao) > 30 else obj.descricao
    # Define o nome da coluna que aparecerá na interface do Django Admin
    descricao_preview.short_description = 'descricao'
    
    # Método para exibir uma prévia do campo 'descricao'
    def sistema_preview(self, obj):
        return obj.sistema[:30] + '...' if obj.sistema and len(obj.descricao) > 30 else obj.sistema
    sistema_preview.short_description = 'sistema'
    
    # Método para exibir uma prévia do campo 'descricao'
    def efeito_preview(self, obj):
        return obj.efeito[:30] + '...' if obj.efeito and len(obj.efeito) > 30 else obj.efeito
    efeito_preview.short_description = 'efeito'
    
    search_fields = ('nome', 'disciplina')
    
    

