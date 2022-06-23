from django.db import models

# Create your models here.
class Pagamento(models.Model):
    valor_pag = models.IntegerField
    forma_pag = models.CharField(max_length=100) 
    parcelas = models.IntegerField
    data_pag = models.DateField(max_length=100)
    banco_pag = models.CharField(max_length=100) 
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome