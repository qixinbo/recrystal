from django.contrib import admin
from .models import *
# Register your models here.
class MeshAdmin(admin.ModelAdmin):
	list_display = ('xmax','ymax', 'zmax')	
admin.site.register(Mesh, MeshAdmin)

class ICAdmin(admin.ModelAdmin):
	list_display = ('op_num', 'grain_num')	
admin.site.register(IC, ICAdmin)

class MaterialsAdmin(admin.ModelAdmin):
	list_display = ('Q', )
admin.site.register(Materials, MaterialsAdmin)

class ExecutionerAdmin(admin.ModelAdmin):
	list_display = ('dt', 'end_time')
admin.site.register(Executioner, ExecutionerAdmin)

class OutputsAdmin(admin.ModelAdmin):
	list_display = ('exodus', 'csv')
admin.site.register(Outputs, OutputsAdmin)