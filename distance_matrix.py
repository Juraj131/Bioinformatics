from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from Bio import SeqIO
import numpy as np
from Bio.Seq import Seq

alignment = AlignIO.read('zarovnane_cytb.aln-fasta', 'fasta')
list_align = []
for align in alignment:
    list_align.append(align)

print(list_align)
calculator = DistanceCalculator('identity')
distances = calculator.get_distance(alignment)
print(calculator)
print(distances)