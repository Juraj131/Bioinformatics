from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from Bio import SeqIO
import numpy as np
from Bio.Seq import Seq
from Bio import Phylo

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
alignment = AlignIO.read('zarovnane_cytb.aln-fasta', 'fasta')
list_align = []


calculator = DistanceCalculator('identity')
distances = calculator.get_distance(alignment) #tu sa vypocitaju vzdialenosti

constructor = DistanceTreeConstructor()
tree = constructor.upgma(distances)
Phylo.draw_ascii(tree) #tu sa nakrelsi strom
Phylo.draw(tree)

Phylo.write(tree, 'nazev.newick','newick')