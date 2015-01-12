from django.db import models

class Mensajero(models.Model):
	nombres = models.CharField(max_length=120)

	def __unicode__(self):
		return self.nombres