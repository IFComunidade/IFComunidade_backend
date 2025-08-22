from django.contrib.auth.models import AbstractUser
from django.db import models
from usuario.managers import UsuarioManager, AlunoManager, SetorManager

class Usuario(AbstractUser):

    class TipoUsuario(models.TextChoices):
        ALUNO = "ALUNO", "Aluno"
        SETOR = "SETOR", "Setor"
        
    tipo = models.CharField(max_length=50, choices=TipoUsuario.choices, default=TipoUsuario.ALUNO)
    
    objects = UsuarioManager()
    
class Aluno(Usuario):
    objects = AlunoManager()
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = Usuario.TipoUsuario.ALUNO
        return super().save(*args, **kwargs)
    
class Setor(Usuario):
    objects = SetorManager()
    class Meta:
        proxy = True
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.tipo = Usuario.TipoUsuario.SETOR
        return super().save(*args, **kwargs)