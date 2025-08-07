from django.contrib import admin
from .models import Projeto, Tarefa

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_termino', 'status')
    list_filter = ('status',)
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'responsavel', 'projeto', 'prazo', 'status')
    list_filter = ('status',)
    search_fields = ('titulo', 'responsavel__username', 'projeto__nome')
