from django.db import models

# Create your models here.
class Servicios(models.Model):
    Servicio_ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Descripcion = models.TextField()
    Costo = models.DecimalField(max_digits=10, decimal_places=2)
    Activo = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre