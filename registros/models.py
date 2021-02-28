from django.db import models
from django.utils import timezone
from predios.models import Predios
from propietarios.models import Propietarios

# Create your models here.


class Registros(models.Model):
    predio = models.ForeignKey(Predios, on_delete=models.CASCADE)
    propietarios = models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edicion")

    
    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"
        ordering = ["-created"]
        
        

    def __str__(self):
        return "{} {}".format(self.predio, self.propietarios)


