import os
import numpy
import sys
sys.path.append(os.environ["COVALIB"])
from Code import *
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold

def main(name, argv):
        if not len(argv) == 2:
                print_usage(name)
                return

	with open(argv[0], 'r') as f:
            lines = f.readlines()
        smiles = [line.split()[0] for line in lines]

        molecules = list(map(lambda smile: [smile, Chem.MolFromSmiles(smile)], smiles))
        molecules = [m for m in molecules if m[1] is not None]

	with open(argv[1], 'w') as f:
		for mol in molecules:
			core = MurckoScaffold.GetScaffoldForMol(mol[1])
			f.write(Chem.MolToSmiles(core) + '\n')

def print_usage(name):
        print "Usage : " + name + " <smiles> <output>"

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])

