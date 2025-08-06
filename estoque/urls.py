from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/editar/<int:pk>/', views.produto_update, name='produto_update'),
    path('produtos/excluir/<int:pk>/', views.produto_delete, name='produto_delete'),

    path('movimentacoes/', views.movimentacao_list, name='movimentacao_list'),
    path('movimentacoes/nova/', views.movimentacao_create, name='movimentacao_create'),
]
