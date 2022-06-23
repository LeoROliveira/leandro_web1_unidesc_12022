from django.db import models

# Create your models here.
class Transferencia(models.Model):
    tipo = models.CharField(max_length=100)
    codIdentificacao = models.CharField(max_length=100) 
        

    def __str__(self):
        return self.nome