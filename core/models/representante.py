from django.db import models
from .setor import Setor
from .pessoa import Pessoa

class Representante (models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.setor}"