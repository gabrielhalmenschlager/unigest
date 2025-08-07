from django.urls import path
from .views import (
    CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView,
    InscricaoListView, InscricaoCreateView, InscricaoUpdateView, InscricaoDeleteView
)

app_name = 'cursos'

urlpatterns = [
    # Cursos
    path('', CursoListView.as_view(), name='curso-list'),  # vai responder em /cursos/
    path('novo/', CursoCreateView.as_view(), name='curso-create'),  # /cursos/novo/
    path('<int:pk>/editar/', CursoUpdateView.as_view(), name='curso-update'),  # /cursos/1/editar/
    path('<int:pk>/excluir/', CursoDeleteView.as_view(), name='curso-delete'),

    # Inscrições
    path('inscricoes/', InscricaoListView.as_view(), name='inscricao-list'),  # /cursos/inscricoes/
    path('inscricoes/novo/', InscricaoCreateView.as_view(), name='inscricao-create'),
    path('inscricoes/<int:pk>/editar/', InscricaoUpdateView.as_view(), name='inscricao-update'),
    path('inscricoes/<int:pk>/excluir/', InscricaoDeleteView.as_view(), name='inscricao-delete'),
]
