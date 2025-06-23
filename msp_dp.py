import numpy as np

def MSSP_calculation(vector):
    n = len(vector)
    S = [vector[0]] #prvy provok opisem
    P = [1] #prvy prvok je vzdy 1

    for i in range(1, n):
        if vector[i] + S[i-1] >= vector[i]: #vlozim do S prvok ktory je suctom prvku vectora a predosleho suctu z S
            P.append(1)
            S.append(vector[i] + S[i-1])
        else:
            P.append(0)
            S.append(vector[i]) #vlozim do S prvok s priratanim nuly

    start_index = S.index(max(S)) #-1 pretoze indexujem poctom prvkov ktorych je viac a index ide od nuly
    sum = vector[start_index] #musim zacat prvkov z vektora s indexom maximalneho cisla v S
    while 1:
        if P[start_index] == 0: #skonci sa tento cyklus ked sa tam vyskytne nula v P
            break
        else:
            sum += vector[start_index - 1] #prirata to posledny prvok ten ktory v P ma nulu lebo to priratava start_idnex -1
            start_index -= 1 #posuvam sa o jeden index dozadu

    return f'MSSP je {sum}'


x = MSSP_calculation([3,2,-6,5,2,-3,6,-4,2,1])
print(x)