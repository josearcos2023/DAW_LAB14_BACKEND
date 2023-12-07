from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    horas_trabajadas = models.PositiveIntegerField()
    pago = models.PositiveIntegerField()

    class Meta:
        ordering = ['nombre']