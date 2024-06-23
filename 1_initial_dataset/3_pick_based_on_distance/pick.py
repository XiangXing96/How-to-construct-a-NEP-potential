"""
Select structures
===========================

This example shows how to select structures from dataset. Ajust min_distance in 22nd line to modify the number of selected structures.
"""
from pynep.calculate import NEP
from pynep.select import FarthestPointSample
from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from pynep.io import load_nep
from ase import Atoms
import copy


a = read('./rough.traj', index=':')
calc = NEP("nep.txt")
print(calc)
des = np.array([np.mean(calc.get_property('descriptor', i), axis=0) for i in a])
sampler = FarthestPointSample(min_distance=0.02)
selected_i = sampler.select(des, [])
write('selected_200.traj', [a[i] for i in selected_i])
print(len(selected_i))
#print(selected_i)
reducer = PCA(n_components=2)
reducer.fit(des)
proj = reducer.transform(des)
plt.scatter(proj[:,0], proj[:,1], label='all data')
selected_proj = reducer.transform(np.array([des[i] for i in selected_i]))
plt.scatter(selected_proj[:,0], selected_proj[:,1], label='selected data')
plt.legend()
plt.axis('off')
plt.savefig('select.png')

select = read('selected.traj', index=':')
write('selected.xyz', [i for i in select])
