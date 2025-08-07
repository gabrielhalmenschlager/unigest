from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero', 'ano_publicacao', 'isbn', 'quantidade']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['aluno', 'livro', 'data_devolucao', 'status']

    def clean(self):
        cleaned_data = super().clean()
        livro = cleaned_data.get('livro')
        status = cleaned_data.get('status')

        if status == 'ativo' and livro and livro.quantidade < 1:
            raise forms.ValidationError('Não há livros disponíveis para empréstimo.')

        return cleaned_data
