from django.db import models

class Parte(models.Model):
	numero_de_parte = models.CharField(max_length=60, primary_key=True)
	descripcion = models.CharField(max_length=120)
