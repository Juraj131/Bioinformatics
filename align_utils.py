import numpy as np
from Bio import Align
from Bio import SeqIO

aligner = Align.PairwiseAligner(match_score = 2.0, gap_score = -3, mismatch_score = -1) # kebyze nic nedam do zatvorky tak je to defaultne
print(aligner)
print(aligner.mode) #hovori v ktorom rezime zarovnavame takz eci globalne alebo lokalne= global lokal
print(aligner.algorithm) #zistime presne na ktorom algoritme to pocita

target = 'AGGGTCT'
query = 'GAAT'

alignments = aligner.align(target, query)
print(alignments) #toto zobrazi len ze odniekial to mame treba to prechadzat vo for cykle alebo dat to do listu

#print(alignments[0])

print(len(alignments))
for align in alignments: #to vedla tych sekvencii tie ciskla su dlzky sekvencii
    print(align)

score = aligner.score(target, query)
print(score) #vypise skore konecne


# alignments = aligner.align(target, query)
# scores = aligner.score(target, query)
# for i in range(len(alignments)):
#     print(alignments[i])
#     print(scores[i])