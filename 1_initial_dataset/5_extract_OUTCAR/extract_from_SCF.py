"""
modify the path and the numbe inf 14th line.

"""
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
from pynep.io import load_nep,dump_nep

a = []
parent_folder = '/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/5_aimd/6_single_point_calculation/DFT_calculation'

for i in range(469):
	file = parent_folder + '/' + str(i+1) + '/OUTCAR'
	print(file)
	temp = read(file, index=':')
	print(len(temp))
	for j in temp:
		a.append(j)
		
print(len(a))
write('rough_train.xyz', [i for i in a])
write('rough_train.traj', [i for i in a])
