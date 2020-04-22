import os
from cluster_functions import cluster_dp
import json
import time

DATA_DIRECTORY = os.path.abspath('data')
RESULTS_DIRECTORY = os.path.abspath('results')

def get_res(pdb):
    """
    params: pdb file in list of lines
    returns: dictionary, keys = residues, values = unweighted centre of mass

    """
    res_num = []
    all_res = {}
    for line in pdb:				# get the number of atoms in the protein
        if line.startswith('ATOM'):
            res_num.append(int(line[23:26]))
    for i in range(min(res_num), max(res_num)+1): # loop through all residues in the protein
        x = 0
        y = 0
        z = 0
        n = 0
        for line in pdb:
            if line.startswith('ATOM'):
                if int(line[23:26]) == i:	# if this atom belongs to the residue we are looking at	
                    residue = line[17:26]  	# get the residue type and number for this atom
                    x += float(line[30:38].strip())	# add the atoms of that residue to a running total
                    y += float(line[38:46].strip())
                    z += float(line[46:54].strip())
                    n += 1
        try:
            all_res[residue] = [x/n, y/n, z/n]	# set unweighted centre of mass for this residue
        except ZeroDivisionError:
            pass
    return all_res		# return unweighted centre of masses for all residues in the given pdb file




for dir in os.listdir(DATA_DIRECTORY):
    all_clusters = {}
    if dir not in os.listdir(RESULTS_DIRECTORY):
        os.makedirs(os.path.join(RESULTS_DIRECTORY, dir))
    coms = {}
    idents = []
    lam = 2.5
    for filename in os.listdir(os.path.join(DATA_DIRECTORY, dir)):
        pdb = open(os.path.join(DATA_DIRECTORY, dir, filename), 'r').readlines()
        coms[filename] = get_res(pdb)
        idents.append(filename)
    for i in coms[idents[0]]:
        print('clustering', i)
        vectors = []
        for j in coms:
            vectors.append(coms[j][i])
        clusters = cluster_dp(vectors, lam, idents)
        all_clusters[i] = clusters
    
    json.dump(all_clusters, open(os.path.join(RESULTS_DIRECTORY, dir, 'residue_clusters.json'), 'w'))
    print('clustered and saved')

