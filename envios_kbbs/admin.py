from django.contrib import admin
from .models import Envio

class EnvioAdmin(admin.ModelAdmin):
	list_display = ('sro', 'parte', 'fecha_envio', 'get_number_parte', 'waybill', 'show_thumbnail', 'responsable_dhl',)
	raw_id_fields = ('parte',)
	search_fields = ['parte__numero_de_parte', 'parte__descripcion', 'sro',]


admin.site.register(Envio, EnvioAdmin)