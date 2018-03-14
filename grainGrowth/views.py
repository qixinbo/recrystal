from django.shortcuts import render
from .models import *
import os
import signal
import subprocess
# Create your views here.

def index(request):
	os.chdir("/home/qixinbo/projects/moose/modules/phase_field/examples/grain_growth")
	if request.method == 'POST':
		mesh = MeshForm(request.POST)
		initial_condition = ICForm(request.POST)
		materials = MaterialsForm(request.POST)
		executioner = ExecutionerForm(request.POST)
		outputs = OutputsForm(request.POST)
		if mesh.is_valid() and initial_condition.is_valid() and materials.is_valid() \
		and executioner.is_valid() and outputs.is_valid():
			me = mesh.save()
			ic = initial_condition.save()
			ma = materials.save()
			ex = executioner.save()
			ou = outputs.save()
			shell_command = (
				"../../phase_field-opt -i grain_growth_2D_voronoi.i "
				"Mesh/dim=%d Mesh/nx=%d Mesh/ny=%d Mesh/nz=%d Mesh/xmin=%d Mesh/ymin=%d Mesh/zmin=%d Mesh/xmax=%d Mesh/ymax=%d Mesh/zmax=%d Mesh/uniform_refine=%d "
				"GlobalParams/op_num=%d GlobalParams/var_name_base=%s UserObjects/voronoi/grain_num=%d Materials/CuGrGr/T=%f "
				"Materials/CuGrGr/GBmob0=%f Materials/CuGrGr/GBenergy=%f Materials/CuGrGr/Q=%f Materials/CuGrGr/wGB=%f "
				"Executioner/solve_type=%s Executioner/TimeStepper/dt=%f Executioner/end_time=%f Executioner/l_max_its=%d Executioner/l_tol=%f Executioner/nl_max_its=%d Executioner/nl_abs_tol=%f Executioner/nl_rel_tol=%f " 
				"Outputs/exodus=%s Outputs/csv=%s"
				%(me.dim, me.nx, me.ny, me.nz, me.xmin, me.ymin, me.zmin, me.xmax, me.ymax, me.zmax, me.uniform_refine,
					ic.op_num, ic.var_name_base, ic.grain_num, ic.T,
					ma.GBmob0, ma.GBenergy, ma.Q, ma.wGB, 
					ex.solve_type, ex.dt, ex.end_time, ex.l_max_its, ex.l_tol, ex.nl_max_its, ex.nl_abs_tol, ex.nl_rel_tol, 
					ou.exodus, ou.csv
					)
				)
			print shell_command
			p = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

	else:
		mesh = MeshForm()
		initial_condition = ICForm()
		materials = MaterialsForm()
		executioner = ExecutionerForm()
		outputs = OutputsForm()

	return render(request, 'grainGrowth/index.html', 
		{
			"mesh_form":mesh,
			"ic_form":initial_condition,
			"materials_form":materials,
			"executioner_form":executioner,
			"outputs_form":outputs
		})