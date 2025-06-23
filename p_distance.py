from Bio import Align
from Bio import SeqIO
import numpy as np
from Bio.Seq import Seq
def p_dist_calculation(name):
    zaznam = list(SeqIO.parse(name, 'fasta')) #pouzil som parse ale a sa aj read v pripade ze by boli sekvence rovnakej dlzky
    sequences = []
    for s in range(len(zaznam)):
        sequences.append(zaznam[s].seq)
    print(zaznam)
    m = len(zaznam)
    print(m)
    P = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            seq1 = sequences[i]
            seq2 = sequences[j]
            n_mutations = 0
            for z in range(len(seq1)):
                if seq1[z] != seq2[z]:
                    n_mutations += 1
            p_dist = n_mutations / len(seq1)
            P[i,j] = p_dist

    return P

#######################################
P = p_dist_calculation('zarovnane_cytb.aln-fasta')
print(P)

