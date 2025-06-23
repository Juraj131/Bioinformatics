from collections import Counter

seq = 'AAACG'
occurance = Counter(seq)
print(occurance) #pocita kde je kolko a akych nukleotidov
print(occurance.most_common(1)[0][0]) #vyindexovanie znaku z listu ktory vznikne
#ta jednotka znemana ze koko znakov najcastejsich chcem , ta prva indexova nula je ze vlezem do listu a zoberiem prvy najcastejsi znak a dlasia nula zoberiem ten znak