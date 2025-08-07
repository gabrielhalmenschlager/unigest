# cursos/models.py

from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    instrutor = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('concluido', 'Concluído'),
    ]

    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        unique_together = ['aluno', 'curso']

    def __str__(self):
        return f"{self.aluno.username} - {self.curso.nome}"
