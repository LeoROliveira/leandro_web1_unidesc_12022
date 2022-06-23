from django.db import models

# Create your models here.
class Pessoa(models.Model):
    matricula = models.IntegerField
    telefone = models.CharField(max_length=100) 
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100) 
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome