import numpy as np
import math

def cum_phase(seq):

    number_phase = []
    
    
    if seq[0] == 'A':
        number_phase.append(math.pi / 4)
        
    elif seq[0] == 'T':
        number_phase.append(-math.pi / 4)
      
    elif seq[0] == 'G':
        number_phase.append(3*math.pi / 4)
      
    elif seq[0] == 'C':
        number_phase.append(-3*math.pi / 4)
        
  
    for i in range(1, len(seq)):
        if seq[i] == 'A':
            number_phase.append(math.pi / 4)
        elif seq[i] == 'T':
            number_phase.append(-math.pi / 4)
        elif seq[i] == 'G':
            number_phase.append(3*math.pi / 4)
        else:
            number_phase.append(-3*math.pi / 4)

    for z in range(1, len(number_phase)):
        number_phase[z] = number_phase[z] + number_phase[z - 1]



    return number_phase
#######################################
x = cum_phase('ATTGCTAAC')
print(x)