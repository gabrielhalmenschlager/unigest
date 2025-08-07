from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),

    # Autenticação (login, logout, password_change etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Redireciona a raiz para a página principal (altere conforme necessidade)
    path('', RedirectView.as_view(url='/biblioteca/', permanent=False)),

    # Rotas dos módulos (apps)
    path('biblioteca/', include('biblioteca.urls')),
    path('cursos/', include('cursos.urls')),
    path('estoque/', include('estoque.urls')),
    path('tarefas/', include('tarefas.urls')),
]

