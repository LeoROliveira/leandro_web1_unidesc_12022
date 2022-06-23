from tokenize import Double
from django.db import models

# Create your models here.
class Imovel(models.Model):
    matricula_imo = models.IntegerField
    rua_imo = models.CharField(max_length=100) 
    cep_imo = models.CharField(max_length=100)
    bairro_imo = models.CharField(max_length=100) 
    cidade_imo = models.DateField(max_length=100)
    uf_imo = models.CharField(max_length=100) 
    tamanho_imo = models.CharField(max_length=100)
    comodos_imo = models.CharField(max_length=100) 
    garagem_imo = models.DateField(max_length=100)
    valor_imo = models.IntegerField
    tipo_imo = models.CharField(max_length=100)
    status_imo = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.nome

    def incluir_Anuncio(cls) -> None:
        return

    def consultar_Anuncio(cls) -> Double:
        return

    def alterar_Anuncio(cls) -> None:
        return

    def remover_Anuncio(cls) -> None:
        return