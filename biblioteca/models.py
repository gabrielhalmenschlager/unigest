from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_publicacao = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

class Emprestimo(models.Model):
    STATUS_ATIVO = 'ativo'
    STATUS_DEVOLVIDO = 'devolvido'
    STATUS_CHOICES = [
        (STATUS_ATIVO, 'Ativo'),
        (STATUS_DEVOLVIDO, 'Devolvido'),
    ]

    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_ATIVO)

    def __str__(self):
        return f"{self.livro.titulo} - {self.aluno.username}"
