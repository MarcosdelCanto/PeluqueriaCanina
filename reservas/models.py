from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField (max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=15)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.nombre_cliente} - {self.servicio} - {self.fecha} - {self.hora}'    