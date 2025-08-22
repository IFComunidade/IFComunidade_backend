from django.contrib.auth.models import AbstractUser
from django.db import models
from usuario.managers import UsuarioManager

class Usuario(AbstractUser):

    class TipoUsuario(models.TextChoices):
        ALUNO = "ALUNO", "Aluno"
        SETOR = "SETOR", "Setor"
        
    tipo = models.CharField(max_length=50, choices=TipoUsuario.choices, default=TipoUsuario.ALUNO)
    
    objects = UsuarioManager()
    
    