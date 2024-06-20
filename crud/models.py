from django.db import models
import datetime

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.titulo
