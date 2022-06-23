from django.db import models

# Create your models here.
class PessoaFisica(models.Model):
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100) 
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100) 
    dataNascimento = models.DateField(max_length=100)
    
    def __str__(self):
        return self.nome