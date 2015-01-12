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

	def __unicode__(self):
		return (self.parte + ' - ' + sel.sro)

	def get_number_parte(self):
		return self.parte.numero_de_parte


	get_number_parte.short_description = 'Numero de Parte'

	
