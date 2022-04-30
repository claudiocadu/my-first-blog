# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel

class Edicao(TimeStampedModel):
    nome = models.CharField(max_length=255, verbose_name= 'Edição')
    descricao = models.TextField(verbose_name= 'Descrição',max_length=300, null = True, blank=True)
    file = models.FileField(upload_to='informativo/')
    data_publicacao = models.DateTimeField(verbose_name= 'Data da Publicação')
    class Meta:
        ordering = ("-data_publicacao",)
        verbose_name = "edição"
        verbose_name_plural = "edições"

    def __str__(self):
        return self.nome