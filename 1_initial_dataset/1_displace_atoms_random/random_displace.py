"""
Select structures
===========================

This example shows how to select structures from dataset
"""
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
import copy
from hiphive.structure_generation import generate_mc_rattled_structures

N_rattle = 200
a = read('new_train.xyz', index=':')
N_str = len(a)

print(N_str)
inter = int(N_str / N_rattle)

initial = []
for i in range(0, N_str, inter):
	initial.append(a[i])

rattle_std = 0.04
d_min = 1.9
n_iter = 50

rattled_supercells = []
for i in initial:
	temp_rattled = generate_mc_rattled_structures(i, n_structures=1, rattle_std=rattle_std, d_min=d_min, n_iter=n_iter)
	for j in temp_rattled:
		rattled_supercells.append(j)

print(len(rattled_supercells))
write("rattled_structure.xyz", [i for i in rattled_supercells])
