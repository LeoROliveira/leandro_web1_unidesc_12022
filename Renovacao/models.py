from django.db import models

# Create your models here.
class Renovacao(models.Model):
    dataDesocupacao = models.DateField(max_length=100)
    dataRenovacao = models.DateField(max_length=100) 
    cartorio = models.CharField(max_length=100)     

    def __str__(self):
        return self.nomev