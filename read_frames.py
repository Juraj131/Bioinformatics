from Bio.Seq import Seq

#cteci ramce 6 ctecich ramcu 3 na vedoucim a tri na komplementarnom
#otevreni cteci ramec zacina start kodonem a koncim na stop kodone
#qrf finder si viem skontrolovat ci to naslo dobry cteci ramec

#na vstupu budu mit nukleotidovou sequenci
# udelat jeji raversni komplement
# seznam sequenci 6 seq lebo 6 ctecich ramcov 3 z original seq a 3 z rcomplement
#seq[0:], seq[1:]
# budem prechadzat po trojiciach tie ulozene sekvence budem sa pytat ci to nie je moj start kodon
#ak najdem zaciatok tak zacnem od najdeneho startu prechadzat dalej po trojiciach a hladat ci nemam nejaky stop kodon
# nasledne tuto sequenci prelozim do proteinov
# nasledne idem do dalsich sekvenci


def QRF(sequence):
    #vytvorenie ctecich ramcov
    list_seq = []
    for z in range(0,3):
        list_seq.append(sequence[z:])
        list_seq.append(sequence.reverse_complement()[z:])
    print(list_seq)

    # start = 'ATG'
    # stop = 'TAA'
    # stop2 = 'TAG'
    # stop3 = ('TGA')

    list_proteins = []


    for seq in list_seq:
        for i in range(0, len(seq),3): #s krokom 3
            if seq[i:i+3] == 'ATG':
                start = i
                new_seq = seq[start:]
                break
            
        for j in range(start + 3, len(new_seq) - 3, 3): # tri na zaciatku lebo vynechavam start kodon
            if seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
                stop = j + 3
                break
        
        list_proteins.append(seq[start:stop].translate())

                
    return list_proteins

x = QRF(Seq('GGATGCGATGACTTACATG"'))
print(x)





