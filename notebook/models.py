from django.db import models

# Create your models here.
class Note(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    secao = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo