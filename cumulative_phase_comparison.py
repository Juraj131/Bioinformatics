import numpy as np
import math
from phase_coordinates import nt2kvad
import matplotlib.pyplot as plt

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord

def fasta_cumulative_kvad(file):
    record = SeqIO.read(file, 'fasta')
    seq = record.seq
    id = record.id
    z = nt2kvad(seq)
    x = z[0]
    y = z[1]
    return x, y, id

x1,y1,id1 = fasta_cumulative_kvad('cox3_bos_taurus.fasta')
x2,y2,id2 = fasta_cumulative_kvad('cox3_canis_lupus.fasta')
x3,y3,id3 = fasta_cumulative_kvad('cox3_cerevisiae.fasta')
x4,y4,id4 = fasta_cumulative_kvad('cox3_drosophila.fasta')
x5,y5,id5 = fasta_cumulative_kvad('cox3_octopus.fasta')
x6,y6,id6 = fasta_cumulative_kvad('cox3_troglodytes.fasta')


    

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(x1, y1, label=id1, color='blue')  # Zobrazenie kumulovanej fázy
plt.plot(x2, y2, label=id2, color='orange')  # Zobrazenie kumulovanej fázy
plt.plot(x3, y3, label=id3, color='red')  # Zobrazenie kumulovanej fázy
plt.plot(x4, y4, label=id4, color='brown')  # Zobrazenie kumulovanej fázy
plt.plot(x5, y5, label=id5, color='green')  # Zobrazenie kumulovanej fázy
plt.plot(x6, y6, label=id6, color='purple')  # Zobrazenie kumulovanej fázy
plt.title('Graf kumulovanej fázy 1. a 4. kvadrantu')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)  # Zobrazenie mriežky
plt.show()