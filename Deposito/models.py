from django.db import models

# Create your models here.
class Deposito(models.Model):
    idDeposito = models.CharField(max_length=100)
       

    def __str__(self):
        return self.nome