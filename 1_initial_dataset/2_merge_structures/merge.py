"""
please modify the path according your environment
"""
#from pynep.io import load_nep,dump_nep
import random
from ase.io import read, write
import numpy as np

all = []

file = "./rattle_structures.xyz"
temp = read(file, ":")
print(file)
print(len(temp))
for j in temp:
	all.append(j)


file = "./aimd.xyz"
temp = read(file, ":")
print(file)
print(len(temp))
for j in temp:
	all.append(j)

print(len(all))


write('new_train.xyz', [i for i in all])
