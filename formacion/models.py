from django.db import models


class Sede(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Ambiente(models.Model):
    codigo = models.CharField(max_length=20)
    capacidad_maxima = models.PositiveIntegerField()
    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
        related_name='ambientes'
    )

    def __str__(self):
        return f"{self.codigo} - {self.sede.nombre}"


class Instructor(models.Model):
    documento = models.CharField(max_length=30, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_institucional = models.EmailField(unique=True)
    ambientes = models.ManyToManyField(
        Ambiente,
        related_name='instructores',
        blank=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"