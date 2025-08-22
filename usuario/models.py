from django.contrib.auth.models import AbstractUser
from .managers import UsuarioManager
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(max_length=120)
    matricula = models.CharField(max_length=10, null= True)

    tipo_usuario = models.CharField(choices=[
        ('SETOR', 'setor'),
        ('ALUNO', 'aluno'),
    ], default='ALUNO')


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if self.tipo_usuario == 'SETOR':
            self.username = self.email
        if self.tipo_usuario == 'ALUNO':
            self.username = self.matricula

    objects = UsuarioManager()
    