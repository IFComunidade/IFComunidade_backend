from django.db import models
from uploader.models import Image
from usuario.models import Usuario

class Postagem(models.Model):

    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=1000)
    data = models.CharField(max_length=15)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="postagens")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
