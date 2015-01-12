from django.db import models
from partes.models import Parte as Parte
from responsables_dhl.models import Mensajero as Mensajero

class Envio(models.Model):
	fecha = models.DateField(auto_now=True)
	parte = models.ForeignKey(Parte)
	sro = models.BigIntegerField(max_length=60)
	fecha_envio = models.DateField(auto_now=True)
	waybill = models.BigIntegerField()
	picture = models.ImageField(upload_to='kbbs')
	responsable_dhl = models.ForeignKey(Mensajero)

	
