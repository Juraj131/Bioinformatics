import numpy as np

def LCS_calculation(sequence):

    m = len(sequence[0]) #riadok
    n = len(sequence[1]) #stlpec

    E = np.zeros((m + 1, n + 1)) #aby sa dal inicializovat prvy riadok a prvy stlpec

    for i in range(1, m+1): #riadok
        for j in range(1,n+1): #stlpec
            #rovnaji sa znaky v sekvenciich
            if sequence[0][i-1] == sequence[1][j-1]:
                E[i,j] = E[i-1,j-1] + 1
            else:
                E[i, j] = max(E[i, j-1], E[i-1, j])

    # zpětná cesta - tvoříme s ní LCS
    LCS = ''
    while 1:
        #podmienka na zastavenie hldadania spatnej cesty
        if i == 0 or j == 0:
            break
        
        #ked sa znaky v sekvenci rovnaju tak pripisem znak tej sekvence do LCS a posuniem sa na diagonale smerom hore
        #v zatvorke sequence musi byt i-1 lebo for ykly isli v dlzke sekvencii plus 1 
        if sequence[0][i-1] == sequence[1][j-1]:
            LCS += sequence[0][i-1]
            i = i - 1
            j = j - 1
        #ked saprvok v matici bude rovnat prvku v matici hore posunieme sa hore 
        #v hranatej zatvorke nemusim davat -1 pretoze sa hybeme v matici ktora ma jeden riadok a stpec navyse
        elif E[i,j] == E[i-1,j]:
            i = i - 1
        #ked to bude inak takze s aprvok rovna prvku zprava tak to znamena ze sa posuniee dolava
        else:
            j = j - 1
    #musim obratit cestu pretoze inakm by bolo odzadu a to nechceme
    LCS = LCS[::-1]

    return E, LCS


############################
x, y = LCS_calculation(['AGTTCGTCT', 'AGAAATG'])
print(x)
print(y)



