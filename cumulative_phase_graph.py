import matplotlib.pyplot as plt
import numpy as np
import math
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from cumulative_phase import cum_phase

record1 = SeqIO.read('lutra.fasta', 'fasta')
record2 = SeqIO.read('rhodo.fasta', 'fasta')


seq1  = record1.seq
seq2 = record2.seq

cum_phase_seq1 = cum_phase(seq1)
cum_phase_seq2 = cum_phase(seq2)

cum_phase_complement1 = cum_phase(seq1.complement())
cum_phase_complement2 = cum_phase(seq2.complement())


plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_seq1)  # Zobrazenie kumulovanej fázy
plt.title('Graf kumulovanej fázy seq lutra')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_seq2)  # Zobrazenie kumulovanej fázy
plt.title('Graf kumulovanej fázy seq rhodo')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_complement1)  # Zobrazenie kumulovanej fázy
plt.title('Graf kumulovanej fázy komplement lutra')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_complement2)  # Zobrazenie kumulovanej fázy
plt.title('Graf kumulovanej fázy komplement rhodo')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_seq2)  # Zobrazenie kumulovanej fázy
plt.plot(cum_phase_complement2)
plt.title('Graf porovnania kumulovanej fázy komplement a seq rhodo')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()

plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
plt.plot(cum_phase_complement1)  # Zobrazenie kumulovanej fázy
plt.plot(cum_phase_seq1)  # Zobrazenie kumulovanej fázy
plt.title('Graf porovnania kumulovanej fázy komplement a seq lutra')
plt.xlabel('Index vzorky')
plt.ylabel('Kumulovaná fáza')
plt.grid(True)  # Zobrazenie mriežky
plt.show()