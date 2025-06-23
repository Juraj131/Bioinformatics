
import numpy as np
import math


def nt2bin(seq):
    B = np.zeros((4,len(seq)))



    for i in range(0,1): #riadky
        for j in range(len(seq)): #stlpce
            if seq[j] == 'A':
                B[i,j] = 1

    j = 0
    for i in range(1,2): #riadky
        for j in range(len(seq)): #stlpce
            if seq[j] == 'C':
                B[i,j] = 1

    j = 0
    for i in range(2,3): #riadky
        for j in range(len(seq)): #stlpce
            if seq[j] == 'G':
                B[i,j] = 1

    j = 0
    for i in range(3,4): #riadky
        for j in range(len(seq)): #stlpce
            if seq[j] == 'T':
                B[i,j] = 1

    return B


#######################################
x = nt2bin('AGTCCTAGC')
print(x)
print(x[0,:])