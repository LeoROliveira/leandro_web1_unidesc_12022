from tokenize import Double
from django.db import models

# Create your models here.
class Funcionario(models.Model):
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100) 
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=100) 
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField
    pis = models.CharField(max_length=100) 
        
    
    def __str__(self):
        return self.nome

    def consultar_Imoveis(cls) -> Double:
        return

    def manter_Anuncio(cls) -> None:
        return

    def manter_Cliente(cls) -> None:
        return

    def manter_Funcionario(cls) -> None:
        return

    def manter_Agendamento(cls) -> None:
        return

    def gerar_Relatorio(cls) -> None:
        return

    def calcular_Salario(cls) -> Double:
        return