from django.urls import path
from .views import (
    ProjetoListView, ProjetoCreateView, ProjetoUpdateView, ProjetoDeleteView,
    TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView
)

app_name = 'tarefas'

urlpatterns = [
    # Projetos
    path('', ProjetoListView.as_view(), name='projeto-list'),  # /tarefas/
    path('novo/', ProjetoCreateView.as_view(), name='projeto-create'),  # /tarefas/novo/
    path('<int:pk>/editar/', ProjetoUpdateView.as_view(), name='projeto-update'),
    path('<int:pk>/excluir/', ProjetoDeleteView.as_view(), name='projeto-delete'),

    # Tarefas
    path('tarefas/', TarefaListView.as_view(), name='tarefa-list'),  # /tarefas/tarefas/
    path('tarefas/novo/', TarefaCreateView.as_view(), name='tarefa-create'),
    path('tarefas/<int:pk>/editar/', TarefaUpdateView.as_view(), name='tarefa-update'),
    path('tarefas/<int:pk>/excluir/', TarefaDeleteView.as_view(), name='tarefa-delete'),
]

