from django.db import models

class Pessoa (models.Model):
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    senha = models.CharField(max_length=12)
    tipo = models.CharField(choices=[
        ('A', 'Aluno'),
        ('S', 'Servidor'),
        ('ADM', 'Adiministrador'),
    ])
    verificado = models.BooleanField

    def __str__(self):
        return f"{self.nome} - {self.tipo} - {self.verificado}"