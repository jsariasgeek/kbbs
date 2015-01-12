from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin as ImportExportModelAdmin
from .models import Parte

class ParteResource(resources.ModelResource):
	class Meta():
		model = Parte
		import_id_fields = ['numero_de_parte']

class ParteAdmin(ImportExportModelAdmin):
	list_display = ('numero_de_parte', 'descripcion', 'dispositivo')
	resource_class = ParteResource



admin.site.register(Parte, ParteAdmin)