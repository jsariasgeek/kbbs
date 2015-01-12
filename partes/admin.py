from django.contrib import admin
from .models import Parte

class ParteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Parte, ParteAdmin)