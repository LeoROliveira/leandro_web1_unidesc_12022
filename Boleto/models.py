from django.db import models

# Create your models here.
class Boleto(models.Model):
    CodCliente = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.nome