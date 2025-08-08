from django.db import models

class TipoSetor (models.Model):
    nome = models.CharField(max_length=120)