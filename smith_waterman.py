#cez numpy where zistim kde mam maximalnu hodnotu v matici
#np.where(S==S.max()) a treba vybrat len jednu suradnicu takze [0]

import numpy as np
from Bio import Align
from Bio import SeqIO


def local_alignment(seq1, seq2, score_system):
    match = score_system[0]
    mismatch = score_system[1]
    gap = score_system[2]

    m = len(seq1)  # riadok
    n = len(seq2)  # stlpec

    S = np.zeros((m + 1, n + 1))  # aby sa dal inicializovat prvy riadok a prvy stlpec

    for i in range(1, m + 1):  # riadok
        for j in range(1, n + 1):  # stlpec
            if seq1[i - 1] == seq2[j - 1]:  # nezabudnut ze sekvencie su posunute o 1
                S[i, j] = max(0, S[i, j - 1] - abs(gap), S[i - 1, j] - abs(gap), S[i - 1, j - 1] + match)
            else:
                S[i, j] = max(0, S[i, j - 1] - abs(gap), S[i - 1, j] - abs(gap), S[i - 1, j - 1] + mismatch)

    zarovnanie_1 = ''  # takze toto je sekvencia 1
    zarovnanie_2 = ''  # sekvencia 2
    x = np.where(S == S.max())
    i = x[0][0] #array([2, 2, 3]), array([3, 4, 2] toto je priklad vystupu kde su v matici tri maxima a staci zobrat jedno
    j = x[1][0] #array([2, 2, 3]), array([3, 4, 2] prvy array su i (riadky) a druhy array su j (stlpce)
    while 1:
        if S[i,j] == 0: #ked sa nejaky prvok bude rovnat 0 v matici tak vysledne zarovnanie lokalne konci
            break
        # najprv potrebujem pri ziskavani spatnej cesty maximum v okoli po odcitani medzier match a mismatch alebo z nuly
        # nasledne sa posuvam v tabulke na zaklade zisteneho maxima
        else:
            if seq1[i - 1] == seq2[j - 1]:
                diagonal = S[i - 1, j - 1] + match
            else:
                diagonal = S[i - 1, j - 1] + mismatch

            # teraz zistime maximum
            maximum = max(S[i - 1, j] - abs(gap), S[i, j - 1] - abs(gap), diagonal) # nepotrebujeme 0 tam vyberat pretoze ked sa najde 0 tak sa to brakne

            # teraz na zaklade zisteneho maxima vyberieme kam sa posunieme v tabulke a priradime sekvencii mezeru alebo nukleotid
            if maximum == diagonal:
                zarovnanie_1 += seq1[i - 1]
                zarovnanie_2 += seq2[j - 1]
                i -= 1
                j -= 1

            elif maximum == S[i - 1, j] - abs(gap): #ked sa to rovna niecomu hore, sipka hore, druha sekvencia delece
                zarovnanie_1 += seq1[i - 1]
                zarovnanie_2 += '-'
                i -= 1

            elif maximum == S[i, j - 1] - abs(gap): #maximum je vlavo, sipka dolava, druha sekvencia inzerce
                zarovnanie_1 += '-'
                zarovnanie_2 += seq2[j - 1]
                j -= 1

    # ovratit
    final_zarovnanie_1 = zarovnanie_1[::-1]
    final_zarovnanie_2 = zarovnanie_2[::-1]

    return S, final_zarovnanie_1, final_zarovnanie_2


##################################################################

#x, y, z =  local_alignment('GTA', 'GATAC', [2, 1, -1])
x, y, z =  local_alignment('TACGT', 'AGTACCC', [3, -1, -3])
print(x)
print(y)
print(z)