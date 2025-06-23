import numpy as np
import math

# A =(1/2 , -√3/2)
# C = (√3/2, 1/2)
# G = (√3/2, -1/2)
# T = (1/2, √3/2)
def nt2kvad(seq):
    number_phase = []

    number_phase_1 = [0]
    for i in range(len(seq)):
        if seq[i] == 'A':
            number_phase_1.append(1/2)
        elif seq[i] == 'T':
            number_phase_1.append(1/2)
        elif seq[i] == 'G':
            number_phase_1.append(math.sqrt(3)/2)
        else:
            number_phase_1.append(math.sqrt(3)/2)

    for z in range(1,len(number_phase_1)):
        number_phase_1[z] = number_phase_1[z] + number_phase_1[z-1]

    number_phase_2 = [0]
    for j in range(len(seq)):
        if seq[j] == 'A':
            number_phase_2.append(math.sqrt(3)/-2)
        elif seq[j] == 'T':
            number_phase_2.append(math.sqrt(3)/2)
        elif seq[j] == 'G':
            number_phase_2.append(-1/2)
        else:
            number_phase_2.append(1/2)

    for p in range(1,len(number_phase_2)):
        number_phase_2[p] = number_phase_2[p] + number_phase_2[p-1]

    number_phase.append(number_phase_1)
    number_phase.append(number_phase_2)
    return number_phase

##############################
x = nt2kvad('TGCAATCGTC')
print(x)