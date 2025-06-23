import numpy as np
import math

def nt2num(seq):
    number_list = []
    for i in range(len(seq)):
        if seq[i] == 'A':
            number_list.append(0)
        elif seq[i] == 'T':
            number_list.append(3)
        elif seq[i] == 'G':
            number_list.append(2)
        else:
            number_list.append(1)
    return number_list
####################
n = nt2num('ATTCGGACT')
print(n)
