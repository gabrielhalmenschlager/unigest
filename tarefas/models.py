from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_termino = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    responsavel = models.CharField(max_length=100)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    prazo = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
