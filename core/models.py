from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    duracao = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()
    foto = models.ImageField(upload_to='docentes/')

    def __str__(self):
        return self.nome