from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from partes.models import Parte as Parte
from responsables_dhl.models import Mensajero as Mensajero

class Envio(models.Model):	
	parte = models.ForeignKey(Parte)
	sro = models.BigIntegerField(max_length=60)
	fecha_envio = models.DateField()
	waybill = models.BigIntegerField()
	picture = models.ImageField(upload_to='kbbs')
	responsable_dhl = models.ForeignKey(Mensajero)
	avatar = ImageSpecField(
			source='picture',
			processors = [ResizeToFill(100,100)],
			format = 'JPEG',
			options = {'quality':100}
		)

	def __unicode__(self):
		return unicode(self.sro)

	def get_number_parte(self):
		return self.parte.numero_de_parte

	def show_thumbnail(self):		
		return """<a><img src='%s' alt='%s'></a>""" %(self.avatar.url, self.sro, self.picture.url)



	get_number_parte.short_description = 'Numero de Parte'
	show_thumbnail.short_description = 'Picture'
	show_thumbnail.allow_tags = True




	
