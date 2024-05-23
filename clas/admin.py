from django.contrib import admin
from .models import Disciplina, Cla

# Regista o modelo de Consulta da tabela completa
admin.site.register(Cla)
admin.site.register(Disciplina)
    