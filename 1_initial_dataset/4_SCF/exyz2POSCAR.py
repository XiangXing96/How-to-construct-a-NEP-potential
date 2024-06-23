"""
Select structures
===========================

This example shows how to select structures from dataset
"""
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt

a = read('train.traj', index=':')
structure_uncalculated = []
parent_folder = './DFT_calculation'
Order = int(len(a))
for i in range(Order):
	file = parent_folder + '/' + str(i+1) + '/POSCAR'
	write(file, a[i], direct=True,sort=True)
