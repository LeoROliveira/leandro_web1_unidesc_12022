from tokenize import Double
from django.db import models

# Create your models here.
class Gerente(models.Model):
    comissao = models.IntegerField
    
    
    def __str__(self):
        return self.nome

    def calcular_Salario(cls) -> Double:
            return