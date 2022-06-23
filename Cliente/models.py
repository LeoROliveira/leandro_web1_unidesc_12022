from tokenize import Double
from typing import Type
from django.db import models

# Create your models here.
class Cliente(models.Model):
    dataCadastro = models.DateField(max_length=100)
    
    
    def __str__(self):
        return self.nome

    def consultar_Imoveis(cls) -> Double:
        return

    def manter_Conta(cls) -> None:
        return

    def agendar_Visita(cls) -> None:
        return