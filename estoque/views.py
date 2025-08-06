from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produto, Movimentacao
from .forms import ProdutoForm, MovimentacaoForm

@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    busca = request.GET.get('busca')
    if busca:
        produtos = produtos.filter(nome__icontains=busca)
    return render(request, 'estoque/produto_list.html', {'produtos': produtos})

@login_required
def produto_create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto cadastrado com sucesso.')
        return redirect('produto_list')
    return render(request, 'estoque/produto_form.html', {'form': form})

@login_required
def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto atualizado com sucesso.')
        return redirect('produto_list')
    return render(request, 'estoque/produto_form.html', {'form': form})

@login_required
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso.')
        return redirect('produto_list')
    return render(request, 'estoque/produto_confirm_delete.html', {'produto': produto})

@login_required
def movimentacao_list(request):
    movimentacoes = Movimentacao.objects.select_related('produto', 'responsavel').order_by('-data')
    return render(request, 'estoque/movimentacao_list.html', {'movimentacoes': movimentacoes})

@login_required
def movimentacao_create(request):
    form = MovimentacaoForm(request.POST or None)
    if form.is_valid():
        movimentacao = form.save(commit=False)
        movimentacao.responsavel = request.user
        try:
            movimentacao.save()
            messages.success(request, 'Movimentação registrada com sucesso.')
            return redirect('movimentacao_list')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'estoque/movimentacao_form.html', {'form': form})
