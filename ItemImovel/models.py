from django.db import models

# Create your models here.
class ItemImovel(models.Model):
    fotos = models.CharField(max_length=100)