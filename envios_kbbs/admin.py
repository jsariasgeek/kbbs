from django.contrib import admin
from .models import Envio

class EnvioAdmin(admin.ModelAdmin):
	pass


admin.site.register(Envio, EnvioAdmin)