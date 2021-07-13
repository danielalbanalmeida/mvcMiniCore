from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    fecha_bono = models.DateField(null=True)
    bono = models.DecimalField(max_digits=5, decimal_places=2)
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
