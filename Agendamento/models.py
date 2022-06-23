from tokenize import Double
from django.db import models

# Create your models here.
class Agendamento(models.Model):
    Dia = models.DateField(max_length=100)
    Hora = models.TimeField(max_length=100) 
    Local = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

    def incluir_Agendamento(cls) -> None:
        return

    def consultar_Agendamento(cls) -> Double:
        return

    def alterar_Agendamento(cls) -> None:
        return

    def remover_Agendamento(cls) -> None:
        return