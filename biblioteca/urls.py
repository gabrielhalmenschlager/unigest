from django.urls import path
from .views import (
    LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView,
    EmprestimoListView, EmprestimoCreateView, EmprestimoUpdateView, EmprestimoDeleteView
)

app_name = 'biblioteca'

urlpatterns = [
    # CRUD Livros
    path('livros/', LivroListView.as_view(), name='livro-list'),
    path('livros/novo/', LivroCreateView.as_view(), name='livro-create'),
    path('livros/<int:pk>/editar/', LivroUpdateView.as_view(), name='livro-update'),
    path('livros/<int:pk>/excluir/', LivroDeleteView.as_view(), name='livro-delete'),

    # CRUD Empréstimos
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimo-list'),
    path('emprestimos/novo/', EmprestimoCreateView.as_view(), name='emprestimo-create'),
    path('emprestimos/<int:pk>/editar/', EmprestimoUpdateView.as_view(), name='emprestimo-update'),
    path('emprestimos/<int:pk>/excluir/', EmprestimoDeleteView.as_view(), name='emprestimo-delete'),
]
