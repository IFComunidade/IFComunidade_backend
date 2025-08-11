from django.db import models
from .setor import Setor

class Postagem(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, related_name="setor")
    TIPO_POSTAGEM_CHOICES = (
        ("A", "Aviso"),
        ("E", "Enquete"),
    )
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=1000)
    tipo_postagem = models.CharField(max_length=1, choices=TIPO_POSTAGEM_CHOICES)
    data = models.DateField()
    imagem = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
