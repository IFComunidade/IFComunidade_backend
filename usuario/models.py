from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Curso
from .managers import CustomUserManager


class Usuario(AbstractUser):
    class TipoUser(models.IntegerChoices):
        ALUNO = 1, "Aluno"
        SETOR = 2, "Setor"
    
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    nome = models.CharField(_("Nome"), max_length=120)
    tipo = models.IntegerField(_("Tipo de usuário"), choices=TipoUser.choices, default=TipoUser.ALUNO)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]


class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=15, unique=True, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="alunos")
    
    def __str__(self):
        return f"{self.usuario.nome} - {self.matricula}"
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        
class Setor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    sigla = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.usuario.nome} ({self.sigla})"
    
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"