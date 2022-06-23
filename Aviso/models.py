from tokenize import Double
from django.db import models

# Create your models here.
class Aviso(models.Model):
    Matricula_avi = models.IntegerField
    Assunto_avi = models.CharField(max_length=100) 
    Data_avi = models.DateField(max_length=100)
    
    def __str__(self):
        return self.nome

    def incluir_Aviso(cls) -> None:
        return

    def consultar_Aviso(cls) -> Double:
        return

    def remover_Aviso(cls) -> None:
        return