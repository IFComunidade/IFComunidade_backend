from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Curso
from .managers import CustomUserManager
from uploader.models import Image


class Usuario(AbstractUser):
    class TipoUser(models.IntegerChoices):
        ALUNO = 1, "Aluno"
        SETOR = 2, "Setor"
    
    foto = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, default=None,)
    username = models.CharField(_("Nome de usuário"), null=True, blank=True)
    email = models.EmailField(_("e-mail address"), unique=True)
    nome = models.CharField(_("Nome"), max_length=120)
    tipo = models.IntegerField(_("Tipo de usuário"), choices=TipoUser.choices, default=TipoUser.ALUNO)
    matricula = models.CharField(_("Matrícula"), max_length=10, unique=True, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=True, blank=True, related_name="alunos")
    cpf = models.CharField(_("CPF"), max_length=14, null=True, blank=True)
    sigla = models.CharField(_("Sigla"), max_length=10, null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        if self.tipo == self.TipoUser.ALUNO:
            return f"{self.nome} - {self.matricula}"
        if self.tipo == self.TipoUser.SETOR:
            return f"{self.nome} ({self.sigla})"
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]