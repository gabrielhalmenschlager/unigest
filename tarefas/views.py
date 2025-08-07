from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Projeto, Tarefa

# Projetos
class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = 'tarefas/projeto_list.html'
    context_object_name = 'projetos'

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    fields = ['nome', 'descricao', 'data_inicio', 'data_termino', 'status']
    template_name = 'tarefas/projeto_form.html'
    success_url = reverse_lazy('tarefas:projeto-list')

class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    fields = ['nome', 'descricao', 'data_inicio', 'data_termino', 'status']
    template_name = 'tarefas/projeto_form.html'
    success_url = reverse_lazy('tarefas:projeto-list')

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    template_name = 'tarefas/projeto_confirm_delete.html'
    success_url = reverse_lazy('tarefas:projeto-list')


# Tarefas
class TarefaListView(LoginRequiredMixin, ListView):
    model = Tarefa
    template_name = 'tarefas/tarefa_list.html'
    context_object_name = 'tarefas'

class TarefaCreateView(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'responsavel', 'projeto', 'prazo', 'status']
    template_name = 'tarefas/tarefa_form.html'
    success_url = reverse_lazy('tarefas:tarefa-list')

class TarefaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'responsavel', 'projeto', 'prazo', 'status']
    template_name = 'tarefas/tarefa_form.html'
    success_url = reverse_lazy('tarefas:tarefa-list')

class TarefaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarefa
    template_name = 'tarefas/tarefa_confirm_delete.html'
    success_url = reverse_lazy('tarefas:tarefa-list')
