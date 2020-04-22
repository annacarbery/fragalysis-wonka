# fragalysis-wonka

A module that clusters key features from ensembles of structures. Originally written by Anthony Bradley.

If you have screened many compounds for binding to your target and have several hits, you can use fragalysis-wonka to cluster ligand pharmacophores, water molecules and ligand movements across the ensemble of structures.

## how to use

Clone the repo and make sure rdkit is installed.

Put your pdb files organised by target in to the 'data' directory (NUDT7A shown as an example).

Run the clustering:
python run_clustering.py

In your 'results' directory there will be a directory for each target and within that, json files listing the different clusters found. For ligands and waters, the larger clusters may highlight interactions of interest with the protein. For residues, the residues that have been moved by several proteins may highlight interactions of interest - i.e. the residues that have 2 or more smaller clusters in the json files. 
