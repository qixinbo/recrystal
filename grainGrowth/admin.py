from django.contrib import admin
from .models import *
# Register your models here.
class MeshAdmin(admin.ModelAdmin):
	list_display = ('xmax','ymax', 'zmax')	
admin.site.register(Mesh, MeshAdmin)

class MaterialsAdmin(admin.ModelAdmin):
	list_display = ('name', )
admin.site.register(Materials, MaterialsAdmin)

class ExecutionerAdmin(admin.ModelAdmin):
	list_display = ('dt', 'end_time')
admin.site.register(Executioner, ExecutionerAdmin)