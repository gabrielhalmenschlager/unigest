from django.contrib import admin
from .models import Livro, Emprestimo

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'ano_publicacao', 'isbn', 'quantidade')
    search_fields = ('titulo', 'autor', 'genero', 'isbn')
    list_filter = ('genero',)

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'aluno', 'data_emprestimo', 'data_devolucao', 'status')
    list_filter = ('status',)
    search_fields = ('livro__titulo', 'aluno__username')
