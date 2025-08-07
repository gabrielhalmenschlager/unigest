from django import forms
from .models import Produto, Movimentacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'preco', 'quantidade']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade', 'responsavel']

    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto')
        tipo = cleaned_data.get('tipo')
        quantidade = cleaned_data.get('quantidade')

        if tipo == 'saida' and produto and quantidade:
            if quantidade > produto.quantidade:
                raise forms.ValidationError('Quantidade de saída maior que o estoque disponível.')

        return cleaned_data
