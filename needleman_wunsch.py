import numpy as np
from Bio import Align
from Bio import SeqIO

def glob_alignment(seq1, seq2, score_system):
    match = score_system[0]
    mismatch = score_system[1]
    gap = score_system[2]

    m = len(seq1)  # riadok
    n = len(seq2)  # stlpec

    S = np.zeros((m + 1, n + 1))  # aby sa dal inicializovat prvy riadok a prvy stlpec
    S[0, :] = np.arange(0, (n + 1) * gap, gap)  # riadok
    S[:, 0] = np.arange(0, (m + 1) * gap, gap)  # sloupec

    for i in range(1, m + 1):  # riadok
        for j in range(1, n + 1):  # stlpec
            if seq1[i-1] == seq2[j-1]: #nezabudnut ze sekvencie su posunute o 1
                S[i,j] = max(S[i,j-1] - abs(gap), S[i-1,j] - abs(gap), S[i-1,j-1] + match)
            else:
                S[i,j] = max(S[i,j-1] - abs(gap), S[i-1,j] - abs(gap), S[i-1,j-1] + mismatch)

    zarovnanie_1 = '' #takze toto je sekvencia 1
    zarovnanie_2 = '' #sekvencia 2
    while 1:
        if i == 0 and j == 0:
            break
        elif i == 0:  # som na prvom riadku musim ist sipkami dolava takze druha sekvencia ma inzercie a prva ma mezery
            zarovnanie_1 += '-'
            zarovnanie_2 += seq2[j - 1]  # pozor sekvence je vzdy posunuta o jedno pretoze tabulka je inicializovana ako m +1
            j -= 1 #psouvam sa v tabulke po prvom stlpci hore

        # pokud jsme v 1. sloupku
        elif j == 0:  # dosiel som na orvy stlpec musim ist sipkami hore do nuly takze druha sekvencia ma mezeru ako deleciu
            zarovnanie_1 += seq1[i - 1] #posuvam sa v sekvencii o jeden prvok dalej 
            zarovnanie_2 += '-'  #delecia v druhej sekvencii
            i -= 1 #posuniem sa v tabulke po prvom stlpci hore
        
        #najprv potrebujem pri ziskavani spatnej cesty maximum v okoli po odcitani medzier match a mismatch
        #nasledne sa posuvam v tabulke na zaklade zisteneho maxima
        else:
            if seq1[i-1] == seq2[j-1]: 
                diagonal = S[i-1,j-1] + match
            else:
                diagonal = S[i-1,j-1] + mismatch
            
            #teraz zistime maximum
            maximum = max(S[i-1,j] - abs(gap), S[i,j-1] - abs(gap), diagonal)

            #teraz na zaklade zisteneho maxima vyberieme kam sa posunieme v tabulke a priradime sekvencii mezeru alebo nukleotid
            if maximum == diagonal:
                zarovnanie_1 += seq1[i-1] #obidve sekvencie maju prvok ani jedna nema mezeru
                zarovnanie_2 += seq2[j-1]
                i -= 1 #posuvame sa diagonalne
                j -= 1

            elif maximum == S[i-1,j] - abs(gap): #ked je maximum zhora tak ideme sipkou hore takze druha sekvencia me deleciu 
                zarovnanie_1 += seq1[i-1]
                zarovnanie_2 += '-'
                i -= 1

            elif maximum == S[i,j-1] - abs(gap): #ked je maximum zlava tak ideme sipkou dolava takze druha sekvencia ma inzerciu
                zarovnanie_1 += '-'
                zarovnanie_2 += seq2[j-1]
                j -= 1

    #ovratit
    final_zarovnanie_1 = zarovnanie_1[::-1]
    final_zarovnanie_2 = zarovnanie_2[::-1]

    return S, final_zarovnanie_1, final_zarovnanie_2
##################################################################

#x,y,z = glob_alignment('TACT', 'AAG', [2, 1, -2])
x,y,z = glob_alignment('ATGTCT', 'GTCGGA', [4, -1, -2])
print(x)
print(y)
print(z)