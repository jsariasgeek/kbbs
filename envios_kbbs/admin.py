from django.contrib import admin
from .models import Envio

class EnvioAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'parte', 'sro', 'fecha_envio', 'waybill', 'picture', 'responsable_dhl',)

admin.site.register(Envio, EnvioAdmin)