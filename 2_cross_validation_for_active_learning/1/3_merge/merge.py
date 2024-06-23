"""

"""
#from pynep.io import load_nep,dump_nep
import random
from ase.io import read, write
import numpy as np

all = []


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/100"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/200"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/300"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/400"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/500"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/600"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if j.info["uncertainty"] < 0.25:
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/1/700/1"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/250"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/275"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/325"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/350"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/375"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/450"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/550"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))

folder = "/media/user/a3b0c976-a8e6-4fb2-9d1c-66c10bc02a32/Simulation/Low-dimension-diffusivity/Li3InCl6/NEP_potential/dataset/11_active_learning_again/1/3_MD/2/650"
for i in range(1):
	file = folder + "/active.xyz"
	try:
		temp = read(file, ":")
		print(file)
		print(len(temp))
		for j in temp:
			#print(j.info["uncertainty"] )

			if (j.info["uncertainty"] < 0.25):
				all.append(j)
			else:
				print(j.info["uncertainty"] )
	except:
		print(file+" is empty")

print(len(all))


write('all_active.xyz', [i for i in all])
