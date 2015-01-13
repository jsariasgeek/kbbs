from django.contrib import admin
from .models import Envio

class EnvioAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'get_number_parte', 'parte', 'sro', 'fecha_envio', 'waybill', 'picture', 'responsable_dhl',)
	raw_id_fields = ('parte',)
	search_fields = ['parte__numero_de_parte', 'parte__descripcion', 'sro',]


admin.site.register(Envio, EnvioAdmin)