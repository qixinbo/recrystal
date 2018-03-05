from django.shortcuts import render
from .models import *
import os
import subprocess
# Create your views here.
def index(request):
	os.chdir("/home/qixinbo/projects/moose/examples/ex01_inputfile")
	if request.method == 'POST':
		mesh = MeshForm(request.POST)
		materials = MaterialsForm(request.POST)
		executioner = ExecutionerForm(request.POST)
		if mesh.is_valid() and materials.is_valid() and executioner.is_valid():
			me = mesh.save()
			ma = materials.save()
			ex = executioner.save()
			shell_command = "mpirun -np 2 ./ex01-opt -i ex01.i Executioner/solve_type=%s" \
			%(ex.solve_type)
			p = subprocess.Popen(shell_command, shell=True)

	else:
		mesh = MeshForm()
		materials = MaterialsForm()
		executioner = ExecutionerForm()

	return render(request, 'grainGrowth/index.html', 
		{"mesh_form":mesh, "materials_form":materials, "executioner_form": executioner})