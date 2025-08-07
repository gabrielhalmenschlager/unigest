from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm

class LivroListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'biblioteca/livro_list.html'
    context_object_name = 'livros'

class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/livro_form.html'
    success_url = reverse_lazy('biblioteca:livro-list')

class LivroUpdateView(LoginRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/livro_form.html'
    success_url = reverse_lazy('biblioteca:livro-list')

class LivroDeleteView(LoginRequiredMixin, DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:livro-list')


class EmprestimoListView(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_list.html'
    context_object_name = 'emprestimos'

class EmprestimoCreateView(LoginRequiredMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'biblioteca/emprestimo_form.html'
    success_url = reverse_lazy('biblioteca:emprestimo-list')

class EmprestimoUpdateView(LoginRequiredMixin, UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'biblioteca/emprestimo_form.html'
    success_url = reverse_lazy('biblioteca:emprestimo-list')

class EmprestimoDeleteView(LoginRequiredMixin, DeleteView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:emprestimo-list')
