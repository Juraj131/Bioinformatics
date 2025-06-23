from Bio import Align

aligner = Align.PairwiseAligner()
#alignments = aligner.align(seq1, seq2)
aligner.mode = 'local'
aligner.match_score = 3 #mal by byt najvacsi
aligner.mismatch_score = 1
aligner.gap_score = -2
print(aligner)

alignments = aligner.align('GATAT', 'AATAT')
#print(alignments[0])
for align in alignments:
    print(align)
