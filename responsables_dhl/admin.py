from django.contrib import admin
from .models import Mensajero

class MensajeroAdmin(admin.ModelAdmin):
	pass


admin.site.register(Mensajero, MensajeroAdmin)