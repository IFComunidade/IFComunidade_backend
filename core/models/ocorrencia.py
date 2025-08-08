from django.db import models

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