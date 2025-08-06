from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Só aplica lógica na criação
            if self.tipo == 'entrada':
                self.produto.quantidade += self.quantidade
            elif self.tipo == 'saida':
                if self.quantidade > self.produto.quantidade:
                    raise ValueError('Estoque insuficiente para saída.')
                self.produto.quantidade -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo.title()} - {self.produto.nome} ({self.quantidade})"
