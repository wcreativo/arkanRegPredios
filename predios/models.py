from django.db import models

# Create your models here.


class Predios(models.Model):
    nombre_Predio = models.CharField(max_length=200)
    num_Matr_Inmob = models.CharField(max_length=200, unique=True)
    Tipo = models.CharField(max_length=200)
    ced_Catastral = models.CharField(max_length=200)
    dir_Predio = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "predio"
        verbose_name_plural = "predios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre_Predio