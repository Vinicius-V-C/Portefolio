from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome