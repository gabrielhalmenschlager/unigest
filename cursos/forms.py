from django import forms
from .models import Curso, Inscricao

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'instrutor', 'carga_horaria', 'categoria']

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['aluno', 'curso', 'status']

    def clean(self):
        cleaned_data = super().clean()
        aluno = cleaned_data.get('aluno')
        curso = cleaned_data.get('curso')

        if Inscricao.objects.filter(aluno=aluno, curso=curso).exists():
            raise forms.ValidationError('Este aluno já está inscrito neste curso.')

        return cleaned_data
