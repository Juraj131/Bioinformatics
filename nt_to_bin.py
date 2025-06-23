import numpy as np
import math
def nt2bin(seq, bit):
    if bit == 2:
        number_2bit = []
        for i in range(len(seq)):
            if seq[i] == 'A':
                number_2bit.append(0)
                number_2bit.append(1)
            elif seq[i] == 'T':
                number_2bit.append(1)
                number_2bit.append(1)
            elif seq[i] == 'G':
                number_2bit.append(0)
                number_2bit.append(0)
            else:
                number_2bit.append(1)
                number_2bit.append(0)
        return number_2bit

    elif bit == 3:
        number_3bit = []
        for j in range(len(seq)):
            if seq[j] == 'A':
                number_3bit.append(0)
                number_3bit.append(1)
                number_3bit.append(0)
            elif seq[j] == 'T':
                number_3bit.append(1)
                number_3bit.append(1)
                number_3bit.append(1)
            elif seq[j] == 'G':
                number_3bit.append(0)
                number_3bit.append(0)
                number_3bit.append(1)
            else:
                number_3bit.append(1)
                number_3bit.append(0)
                number_3bit.append(0)
        return number_3bit

    else:
        return 'invalid number'
##############################
x = nt2bin('TGCAATCGTC',3)
print(x)