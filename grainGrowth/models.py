from django.db import models
from django.forms import ModelForm
# Create your models here.
class Mesh(models.Model):
	dim = models.IntegerField('model dimension', default=2)
	nx = models.IntegerField('No. of elements in x', default=10)
	ny = models.IntegerField('No. of elements in y', default=10)
	nz = models.IntegerField('No. of elements in z', default=0)
	xmin = models.FloatField('min x-coordinate', default=0)
	ymin = models.FloatField('min y-coordinate', default=0)
	zmin = models.FloatField('min z-coordinate', default=0)
	xmax = models.FloatField('max x-coordinate', default=1000)
	ymax = models.FloatField('max y-coordinate', default=1000)
	zmax = models.FloatField('max z-coordinate', default=0)
	uniform_refine = models.IntegerField('initial uniform refinement', default=2)

class IC(models.Model):
	op_num = models.IntegerField('number of order paramaters', default=10)
	grain_num = models.IntegerField('number of grains', default=10)
	var_name_base = models.CharField('base name of grains', default='gr', max_length=10)
	T = models.FloatField('temperature', default=450)

class Materials(models.Model):
	GBmob0 = models.FloatField('mobility prefactor', default=2.5e-6)
	GBenergy = models.FloatField('grain boundary energy', default=0.708)
	Q = models.FloatField('activation energy', default=0.23)
	wGB = models.FloatField('width of grain boundary', default=14)

class Executioner(models.Model):
	solve_type = models.CharField('solver type', default='PJFNK', max_length=20)
	dt = models.FloatField('time step', default=5)
	end_time = models.FloatField('end time', default=4000)
	l_max_its = models.IntegerField('max number of linear iter', default=30)
	l_tol = models.FloatField('relative tol for linear solver', default=1e-4)
	nl_max_its = models.IntegerField('max no. of nonlinear iters', default=40)
	nl_abs_tol = models.FloatField('absolute tol for nonlinear solver', default=1e-11)
	nl_rel_tol = models.FloatField('relative tol for nonlinear solver', default=1e-8)

class Outputs(models.Model):
	isOutput = (('true', 'true'), ('false', 'false'))
	exodus = models.CharField('exodus file is exported?', choices=isOutput, max_length=5, default='true')
	csv = models.CharField('csv file is exported?', choices=isOutput, max_length=5, default='true')

class MeshForm(ModelForm):
	class Meta:
		model = Mesh
		fields = '__all__'

class ICForm(ModelForm):
	class Meta:
		model = IC
		fields = '__all__'

class MaterialsForm(ModelForm):
	class Meta:
		model = Materials
		fields = '__all__'

class ExecutionerForm(ModelForm):
	class Meta:
		model = Executioner
		fields = '__all__'

class OutputsForm(ModelForm):
	class Meta:
		model = Outputs
		fields = '__all__'