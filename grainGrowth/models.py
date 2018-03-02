from django.db import models
from django.forms import ModelForm
# Create your models here.
class Mesh(models.Model):
	dim = models.IntegerField('model dimension', default=2)
	nx = models.IntegerField('number of elements in x-direction', default=10)
	ny = models.IntegerField('number of elements in y-direction', default=10)
	nz = models.IntegerField('number of elements in z-direction', default=0)
	xmin = models.FloatField('minium x-coordinate of the mesh', default=0)
	ymin = models.FloatField('minium y-coordinate of the mesh', default=0)
	zmin = models.FloatField('minium z-coordinate of the mesh', default=0)
	xmax = models.FloatField('maximum x-coordinate of the mesh', default=1000)
	ymax = models.FloatField('maximum y-coordinate of the mesh', default=1000)
	zmax = models.FloatField('maximum z-coordinate of the mesh', default=0)

class Materials(models.Model):
	GBmob0 = models.FloatField('mobility prefactor', default=2.5e-6)
	GBenergy = models.FloatField('grain boundary energy', default=0.708)
	Q = models.FloatField('activation energy', default=0.23)
	T = models.FloatField('temperature', default=450)
	wGB = models.FloatField('width of grain boundary', default=14)

class Executioner(models.Model):
	dt = models.FloatField('time step', default=5)
	end_time = models.FloatField('end time', default=4000)


class MeshForm(ModelForm):
	class Meta:
		model = Mesh
		fields = '__all__'

class MaterialsForm(ModelForm):
	class Meta:
		model = Materials
		fields = '__all__'

class ExecutionerForm(ModelForm):
	class Meta:
		model = Executioner
		fields = '__all__'