from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curso, Inscricao
from .forms import CursoForm, InscricaoForm

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'
    context_object_name = 'cursos'

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('cursos:curso-list')

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('cursos:curso-list')

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('cursos:curso-list')


class InscricaoListView(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = 'cursos/inscricao_list.html'
    context_object_name = 'inscricoes'

class InscricaoCreateView(LoginRequiredMixin, CreateView):
    model = Inscricao
    form_class = InscricaoForm
    template_name = 'cursos/inscricao_form.html'
    success_url = reverse_lazy('cursos:inscricao-list')

class InscricaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Inscricao
    form_class = InscricaoForm
    template_name = 'cursos/inscricao_form.html'
    success_url = reverse_lazy('cursos:inscricao-list')

class InscricaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Inscricao
    template_name = 'cursos:inscricao_confirm_delete.html'
    success_url = reverse_lazy('cursos:inscricao-list')
