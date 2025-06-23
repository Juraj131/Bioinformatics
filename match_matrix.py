

### prevzato a upraveno z MATLAB funkce seqdotplot (https://www.mathworks.com/help/bioinfo/ref/seqdotplot.html)
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO

def seqdotplot(seq1, seq2, window, match):

    seq1 = seq1.upper()
    seq2 = seq2.upper()

    len1, len2 = len(seq1), len(seq2)

    match_matrix = np.zeros((len1 - window + 1, len2 - window + 1))

    for i in tqdm(range(len1 - window + 1)):
        subseq1 = seq1[i:i + window]
        for j in range(len2 - window + 1):
            subseq2 = seq2[j:j + window]
            matches = sum(c1 == c2 for c1, c2 in zip(subseq1, subseq2))
            if matches >= match:
                match_matrix[i, j] = 1

    plt.figure(figsize=(10, 10))
    plt.imshow(match_matrix, cmap='Greys', origin='lower', aspect='auto')
    plt.xlabel(f"Sequence 2 (length {len2} bp)")
    plt.ylabel(f"Sequence 1 (length {len1} bp)")
    plt.title(f"Dot plot (window={window}, match={match})")
    plt.show()


# Example usage
seq1 = SeqIO.read('sapiens_hemo.fasta', 'fasta')
seq2 = SeqIO.read('lenochod.fasta', 'fasta')
seqdotplot(seq1, seq2, 50, 15)