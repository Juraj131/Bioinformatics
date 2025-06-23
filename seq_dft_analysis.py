import matplotlib.pyplot as plt
import numpy as np
import math
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from nt_to_binary import cum_phase
from cviko11.nt_to_binary import nt2bin

def dft(fasta_file):
    record = SeqIO.read(fasta_file, 'fasta')
    seq = record.seq
    V = nt2bin(seq)
    N = len(seq)
    S = []
    for k in range(1,N//2):

        #A
        iv_A = V[0,:]
        A_k = 0
        for n in range(N): #stlpce
            if iv_A[n] != 0:
                exponent = (-2j*np.pi*k*n)/N
                A_k_n = np.exp(exponent)
                A_k += A_k_n
        #C
        n = 0
        C_k = 0
        iv_C = V[1,:]
        for n in range(N): #stlpce
            if iv_C[n] != 0:
                exponent = (-2j*np.pi*k*n)/N
                C_k_n = np.exp(exponent)
                C_k += C_k_n

        #G
        n = 0
        G_k = 0
        iv_G = V[2,:]
        for n in range(N): #stlpce
            if iv_G[n] != 0:
                exponent = (-2j*np.pi*k*n)/N
                G_k_n = np.exp(exponent)
                G_k += G_k_n
        #T
        n = 0
        T_k = 0
        iv_T = V[3,:]
        
        for n in range(N): #stlpce
            if iv_T[n] != 0:
                exponent = (-2j*np.pi*k*n)/N
                T_k_n = np.exp(exponent)
                T_k += T_k_n


        S_k = abs(A_k)**2 + abs(C_k)**2 + abs(G_k)**2 + abs(T_k)**2
        S.append(S_k)


    k_vals = np.arange(1, N // 2)  
    freqs = k_vals / N  # normalizovaná frekvencia

    plt.figure(figsize=(8, 6))  # Nastavenie veľkosti grafu
    plt.plot(freqs,S) 
    plt.title(f'Graf vykonoveho spektra sekvencie {record.id}')
    plt.xlabel('Normalizovana frekvencia [Hz]')
    plt.ylabel('Amplituda spektra [-]')
    plt.show()

 




dft('homo_sapiens_mitochondrion.fasta')
