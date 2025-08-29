from django.db import models
from uploader.models import Image


class Postagem(models.Model):

    TIPO_POSTAGEM_CHOICES = (
        ("A", "Aviso"),
        ("E", "Enquete"),
    )
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=1000)
    tipo_postagem = models.CharField(max_length=1, choices=TIPO_POSTAGEM_CHOICES)
    data = models.DateField()
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
