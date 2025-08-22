from django.db import models
from .usuario import Usuario
from core.models import Curso

class PerfilAluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=15, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} - {self.matricula}"

class PerfilSetor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120, unique=True)
    sigla = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.nome} ({self.sigla})"