from tokenize import Double
from django.db import models

# Create your models here.
class Corretor(models.Model):
    comissao = models.IntegerField
    idCorretor = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.nome

    def calcular_Salario(cls) -> Double:
        return