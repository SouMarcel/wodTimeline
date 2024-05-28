from django.contrib import admin
from .models import Cla

# Register your models here.
class ClaAdmin(admin.ModelAdmin):
    list_display = (
                    'nome', 'historia_preview', 'apelido', 'mote_preview', 'seita_preview', 
                    'aparencia_preview', 'refugio_preview',
            'cria_persona_preview', 'fraquezas_preview', 'organizacao_preview', 
            'antecedentes_preview', 'estereotipos_preview', 'logo', 'disciplinas_list', 'livro',
    )
    # resolver o problema de aprosentar campos M2M (many-to-many field)
    def disciplinas_list(self, obj):
        # Junta os nomes das disciplinas em uma única string, separadas por vírgula
        return ", ".join([disciplina.nome for disciplina in obj.disciplinas.all()])
    # Define o nome da coluna que aparecerá na interface do Django Admin
    disciplinas_list.short_description = 'Disciplinas'


    def historia_preview(self, obj):
        return obj.historia[:30] + '...' if obj.historia and len(obj.historia) > 30 else obj.historia
    # Define o nome da coluna que aparecerá na interface do Django Admin
    historia_preview.short_description = 'historia'

    def mote_preview(self, obj):
        return obj.mote[:30] + '...' if obj.mote and len(obj.mote) > 30 else obj.mote
    # Define o nome da coluna que aparecerá na interface do Django Admin
    mote_preview.short_description = 'mote'
    
    def seita_preview(self, obj):
        return obj.seita[:30] + '...' if obj.seita and len(obj.seita) > 30 else obj.seita
    # Define o nome da coluna que aparecerá na interface do Django Admin
    seita_preview.short_description = 'seita'
    
    def aparencia_preview(self, obj):
        return obj.aparencia[:30] + '...' if obj.aparencia and len(obj.aparencia) > 30 else obj.aparencia
    # Define o nome da coluna que aparecerá na interface do Django Admin
    aparencia_preview.short_description = 'aparencia'
    
    def refugio_preview(self, obj):
        return obj.refugio[:30] + '...' if obj.refugio and len(obj.refugio) > 30 else obj.refugio
    # Define o nome da coluna que aparecerá na interface do Django Admin
    refugio_preview.short_description = 'refugio'
    
    def cria_persona_preview(self, obj):
        return obj.cria_persona[:30] + '...' if obj.cria_persona and len(obj.cria_persona) > 30 else obj.cria_persona
    # Define o nome da coluna que aparecerá na interface do Django Admin
    cria_persona_preview.short_description = 'cria_persona'
    
    def fraquezas_preview(self, obj):
        return obj.fraquezas[:30] + '...' if obj.fraquezas and len(obj.fraquezas) > 30 else obj.fraquezas
    # Define o nome da coluna que aparecerá na interface do Django Admin
    fraquezas_preview.short_description = 'fraquezas'
    
    def organizacao_preview(self, obj):
        return obj.organizacao[:30] + '...' if obj.organizacao and len(obj.organizacao) > 30 else obj.organizacao
    # Define o nome da coluna que aparecerá na interface do Django Admin
    organizacao_preview.short_description = 'organizacao'
    
    def antecedentes_preview(self, obj):
        return obj.antecedentes[:30] + '...' if obj.antecedentes and len(obj.antecedentes) > 30 else obj.antecedentes
    # Define o nome da coluna que aparecerá na interface do Django Admin
    antecedentes_preview.short_description = 'antecedentes'
    
    def estereotipos_preview(self, obj):
        return obj.estereotipos[:30] + '...' if obj.estereotipos and len(obj.estereotipos) > 30 else obj.estereotipos
    # Define o nome da coluna que aparecerá na interface do Django Admin
    estereotipos_preview.short_description = 'estereotipos'
    
    search_fields = (
        'nome', 'livro__nome', 'disciplina__nome' # __nome: procura o campo nome dentro da FK da model
    )
    
    filter_horizontal = ('disciplinas',)
    
admin.site.register(Cla, ClaAdmin)