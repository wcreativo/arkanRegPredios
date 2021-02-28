from django.db import models

# Create your models here.

class Propietarios(models.Model):
    nom_Prop = models.CharField(max_length=200)
    ced_Prop = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "propietario"
        verbose_name_plural = "Propietarios"
        ordering = ["-created"]
        

    def __str__(self):
        return self.nom_Prop