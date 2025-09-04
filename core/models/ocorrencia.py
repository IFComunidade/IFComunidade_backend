from django.db import models
from uploader.models import Image
from usuario.models import Usuario
class Ocorrencia (models.Model):
    titulo = models.CharField(max_length=120)
    texto = models.CharField(max_length=1000)
    class Status(models.IntegerChoices):
       ENTREGUE = 1, "Entregue"
       EM_ANALISE = 2, "Em analise"
       CONCLUIDO_RESOLVIDO = 3, "Concluído"
       CONCLUIDO_NAO_RESOLVIDO = 4, "Concluído não resolvido"

    status = models.IntegerField(choices=Status.choices, default=Status.ENTREGUE)
    anonima = models.BooleanField()
    data = models.DateField(auto_now_add=True)
    tipo_ocorrencia = models.CharField(choices=[
        ('D', 'Denúncia'),
        ('S', 'Sugestão'),
        ('R', 'Reclamação'),
    ])

    setor = models.ForeignKey(
    Usuario,
    on_delete=models.PROTECT,
    related_name='ocorrencias_recebidas',
    limit_choices_to={'tipo': Usuario.TipoUser.SETOR}
)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="ocorrencias")
    
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        
        def __str__ (self):
          return self.titulo