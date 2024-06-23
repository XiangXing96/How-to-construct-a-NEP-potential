#!/bin/bash

for i in {1..469}; 
do
cd /media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/6_single_point_calculation/DFT_calculation
mkdir $i
cd $i
cp /media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/6_single_point_calculation/INCAR .
cp /media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/6_single_point_calculation/POTCAR .
done

cd /media/mee2123/a1d48093-011c-4506-9626-2551684cff1e/data/Li3InCl6/rough_database/6_single_point_calculation
python exyz2POSCAR.py
