import os
from water_clustering import cluster_waters
from ligand_clustering import cluster_ligands
from residue_clustering import cluster_residues

DATA_DIR = os.path.abspath('data')
RESULTS_DIR = os.path.abspath('results')

for target in os.listdir(DATA_DIR):
	print(target)
	print('clustering residues')
	cluster_residues(DATA_DIR, RESULTS_DIR, target)
	print('clustering waters')
	cluster_waters(DATA_DIR, RESULTS_DIR, target)
	print('clustering ligands')
	cluster_ligands(DATA_DIR, RESULTS_DIR, target)
	print('features of ' + target + ' are clustered and saved')	
