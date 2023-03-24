from django.db import models

class Boleta_permiso(models.Model):
    Nombre = models.CharField(max_length=100)
    Motivo = models.TextField(blank=True)

class Users(models.Model):
    Usuario = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)

