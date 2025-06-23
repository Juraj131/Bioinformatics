import numpy as np
from Bio import Align
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from tqdm import tqdm
import numpy as np
import math

def BLOSUM_calculation(set_seq):
    S = len(set_seq) #pocet seq
    W = len(set_seq[0]) #dlzka sekvence
    N = ((S*(S-1))/2) * W #pocet dvojic znaku v bloku (stlpci) resp pocet prvkov v matici, vyuzitie pri normalizacii
    znaky = []
    for seq in set_seq: #spajam znaky do listu jedneho aby som to vedel zoradit podla abecedy
        for znak in seq:
            znaky.append(znak)
    #print(znaky)

    #zistenie unikatnych znakov a zoradenei podla abecedy
    unikatne_znaky = sorted(set(''.join(znaky))) #set je mnozina a odstranuje duplikaty, join spaja pismena v liste do stringu
    m = len(unikatne_znaky)
    #print(unikatne_znaky)

    #prazdna matica o velkosti unikatnych znakov
    F = np.zeros((m,m))
    #print(F)

    #zo stringov sme spravili listy obsahujuce jednotlive pismena
    sequences = [list(seq) for seq in set_seq]
    print(sequences)


    for i in range(m): #riadky
        for j in range(m): #stlpce
            if i == j: #ked sme na diagoonale takze rovnake dva unikatne znaky
                diagonal_znak = unikatne_znaky[i] #ktore cetnosti dvoch rovnakych znakov na diagonale pocitame
                f = 0
                for z in range(W):
                    blok = [pismeno[z] for pismeno in sequences] #prevratenie iteracii na stlpce z riadkov
                    #print(blok)
                    n_diagonal = blok.count(diagonal_znak) #pocitame vyskyt daneho znaku pre vsetky stlpce 
                    #print(n)
                    fii = (n_diagonal*(n_diagonal-1))/2 #vypocet cetnosti na diagonale
                    f += fii
                    F[i,j] = f
            else: #ked nie sme na diagonale
                znak1 = unikatne_znaky[i] #vyberame podla pozicie na ktoru dvojicu znakov porovnavame
                znak2 = unikatne_znaky[j]
                f = 0
                for r in range(W):
                    blok = [pismeno[r] for pismeno in sequences] #prevratenie iteracii na stlpce z riadkov
                    #print(blok)
                    n_znak1 = blok.count(znak1) #pocitame vyskyt daneho znaku pre vsetky stlpce 
                    n_znak2 = blok.count(znak2)
                    #print(n)
                    fij = n_znak1 * n_znak2 #vypocet cetnosti mimo diagonaly
                    f += fij
                    F[i,j] = f

    #maticove delenie              
    Q = F / N #normalizacia cetnosti poctami vseh dvojic v bloku

    #marginalne soucty
    p_hodnoty = []
    i = 0
    j = 0
    for i in range(m):
        p_diagonal = 0
        p_all = 0  #v kazdej iteracii sa to vynuluje aby prebehol novy vypocet
        marg_sum = 0
        for j in range(m):
            if i == j:
                p_diagonal += Q[i,j]
            else:
                p_all += Q[i,j]
        marg_sum = p_diagonal + p_all / 2 #najprv prebehne tento vypocet az pototm zacne dalsi riadok
        p_hodnoty.append(float(marg_sum))

    #kontrukce matice B (blosum)
    i = 0
    j = 0
    B = np.zeros((m,m)) #iniclializacia matice B
    for i in range(m):
        for j in range(m):
            if i == j:
                #vypocet prvku blosum matice
                B[i,j] = Q[i,j] / (p_hodnoty[i] ** 2)
                # aplikace binarneho logaritmu a meritka a zaokruhlenia
                B[i,j] = 2*math.log(B[i,j],2)
                #zaokruhlenie
                B[i,j] = round(B[i,j],0) #na kolko desatinych miest to ma zaokruhlovat
            else:
                #vypocet prvku blosum matice
                B[i,j] = Q[i,j] / (2 * p_hodnoty[i] * p_hodnoty[j])
                # aplikace binarneho logaritmu a meritka a zaokruhlenia
                B[i,j] = 2*math.log(B[i,j],2)
                #zaokruhlenie
                B[i,j] = round(B[i,j],0) #na kolko desatinych miest to ma zaokruhlovat
    #print(F)
    #print(Q)
    #print(p_hodnoty)
    #print(B)
    return F, Q, p_hodnoty, B

########################################################
F, Q, p_hodnoty, B = BLOSUM_calculation(['CAABABA','BBABCBB','AAABCBA'])
print(f'Matica cetnosti: {F}')
print(f'Normovana matica: {Q}')
print(f'Marginalne soucty: {p_hodnoty}')
print(f'Blosum matica: {B}')