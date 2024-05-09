from django.db import models

# Create your models here.
class Product(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField() 
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrepyth