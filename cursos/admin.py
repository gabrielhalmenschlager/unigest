from django.contrib import admin
from .models import Curso, Inscricao

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instrutor', 'categoria', 'carga_horaria')
    search_fields = ('nome', 'instrutor', 'categoria')

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_inscricao', 'status')
    list_filter = ('status',)
    search_fields = ('aluno__username', 'curso__nome')
