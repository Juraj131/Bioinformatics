import numpy as np

def ED_calculation(sequence):

    m = len(sequence[0]) #riadok
    n = len(sequence[1]) #stlpec

    E = np.zeros((m + 1, n + 1)) #aby sa dal inicializovat prvy riadok a prvy stlpec
    E[0, :] = np.arange(0, n+1, 1) #riadok, nulty riadok a vsetky stlpce preto tam davam pocet
    E[:, 0] = np.arange(0, m+1, 1) #sloupec


    for i in range(1, m+1): #riadok 
        for j in range(1,n+1): #stlpec (prechadzam prvy riadok stlpcami)
            #rovnaji sa znaky v sekvenciich
            if sequence[0][i-1] == sequence[1][j-1]:
                match = 0
            else:
                match = 1
            E[i,j] = min(E[i, j-1] + 1, E[i-1, j] + 1, E[i-1, j-1] + match)
            #ED_distance = E[m,n] #toto su indexy tu ratam aj 0
    ED_distance = E[i,j] #toto su indexy tu ratam aj 0
    return E, ED_distance
x, dist = ED_calculation(['AGTTCGTCT', 'AGAAATG'])
print(x)
print(dist)


