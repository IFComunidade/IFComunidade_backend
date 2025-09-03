from django.db import models
from uploader.models import Image
class Ocorrencia (models.Model):
    titulo = models.CharField(max_length=120)
    texto = models.CharField(max_length=1000)
    status = models.CharField(choices=[
        ('E', 'Entregue'),
        ('A', 'Em analise'),
        ('C', 'Concluído'),
    ])
    anonima = models.BooleanField
    data = models.DateField()
    anexo = models.CharField(max_length=40)
    tipo_ocorrencia = models.CharField(choices=[
        ('D', 'Denúncia'),
        ('S', 'Sugestão'),
        ('R', 'Reclamação'),
    ])
    
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

        def __str__ (self):
        return self.titulo