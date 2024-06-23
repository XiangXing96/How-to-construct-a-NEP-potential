"""
Select structures
===========================

merge structures from aimd and extract some structures every 50 structures
"""
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from ase import Atoms
import copy
from ase.md import analysis as traj_analysis


# Read OUTCAR
fcc = []
folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/200"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_200.traj', [i for i in temp])


folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/400"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_400.traj', [i for i in temp])

folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/600"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_600.traj', [i for i in temp])

folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/600/go_on"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_600_go_on.traj', [i for i in temp])

folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/800"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_800.traj', [i for i in temp])

folder = "/media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/1_aimd/1000"
file = folder + "/OUTCAR"
print(file)
temp = read(file, ":")
for j in temp:
	fcc.append(j)
write('aimd_1000.traj', [i for i in temp])

print("Number of fcc:")
print(len(fcc))

all = []
for i in fcc:
	all.append(i)

all_reduced_50 = []
for i in range(0, len(fcc), 50):
	all_reduced_50.append(fcc[i])

write('all.traj', [i for i in all])
write('train.xyz', [i for i in all_reduced_50])
