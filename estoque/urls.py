from django.urls import path
from .views import (
    ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView,
    MovimentacaoListView, MovimentacaoCreateView, MovimentacaoUpdateView, MovimentacaoDeleteView
)

app_name = 'estoque'

urlpatterns = [
    # Produtos
    path('', ProdutoListView.as_view(), name='produto-list'),  # /estoque/
    path('novo/', ProdutoCreateView.as_view(), name='produto-create'),  # /estoque/novo/
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto-update'),
    path('<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto-delete'),

    # Movimentações
    path('movimentacoes/', MovimentacaoListView.as_view(), name='movimentacao-list'),  # /estoque/movimentacoes/
    path('movimentacoes/novo/', MovimentacaoCreateView.as_view(), name='movimentacao-create'),
    path('movimentacoes/<int:pk>/editar/', MovimentacaoUpdateView.as_view(), name='movimentacao-update'),
    path('movimentacoes/<int:pk>/excluir/', MovimentacaoDeleteView.as_view(), name='movimentacao-delete'),
]

