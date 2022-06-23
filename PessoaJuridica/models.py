from django.db import models

# Create your models here.
class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100) 
    representanteLegal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome