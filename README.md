# How-to-construct-a-NEP-potential
The purpose of this guideline is to construct a neuroevolution potential (NEP) to perform molecular dynamics. More details about NEP and the software, GPUMD, can be found in https://gpumd.org/.

To run scripts mentioned in the tutorial, some packages are required:  
(1) Atomic Simulation Environment (https://wiki.fysik.dtu.dk/ase/index.html) is used to read vasp or GPUMD results;  
(2) PyNEP (https://github.com/bigd4/PyNEP) is used to pick structures according to the distance in latent space;  
(3) High-order force constants for the masses (https://hiphive.materialsmodeling.org/) is used to generate structures with random displacement for atoms. 

You can construct a nep through entering the above folders step by step.  
Hope you successful ^_^ !
