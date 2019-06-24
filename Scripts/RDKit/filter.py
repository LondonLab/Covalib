import random
import sys
from rdkit import Chem
from rdkit.Chem import rdChemReactions
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors

def main(name, argv):
    if len(argv) != 4:
        print_usage(name)
        return
    
    MW = float(argv[2])
    RB = int(argv[3])
    MW_min = float(argv[1])

    #read molport building blocks
    with open(argv[0], 'r') as f:
        for line in f:
            line_s = line.split()
            molecule = [Chem.MolFromSmiles(line_s[0]), line_s[1]]
            if molecule[0] == None:
                continue
            if Descriptors.MolWt(molecule[0]) <= MW and rdMolDescriptors.CalcNumRotatableBonds(molecule[0]) <= RB and Descriptors.MolWt(molecule[0]) >= MW_min:
                print line_s[0] + "\t" + line_s[1]
#            else:
#                print Descriptors.MolWt(molecule[0]) <= MW
#                print rdMolDescriptors.CalcNumRotatableBonds(molecule[0])

def print_usage(name):
    print "Usage : " + name + " <library> <min MW> <max MW> <max rotational bonds>"

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])
