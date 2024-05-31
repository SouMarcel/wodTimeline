from django.contrib import admin
from .models import Local

# Register your models here.
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'regiao', 'dimensao_descr', 'era', 'livro'
    )
    list_filter = (
        'livro', 'era'
    )
    search_fields = (
        'nome', 'regiao', 'dimensão'
    )
    
    def dimensao_descr(self, obj):
        return obj.get_dimensao_display()
    dimensao_descr.short_description = 'Dimensao'