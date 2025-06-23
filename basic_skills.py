from Bio.Seq import Seq

#trieda seq
sequence =  Seq('ATGCGCTAGCA')
print(sequence)
seq = 'ATGCGCTAGCA'
print(seq)


#pocitanie poctu v seq
print(len(sequence))

# prechadzanie
for n in sequence:
    print(n)


#indexy nukleotidu cez dlzku sequence
for i in range(len(sequence)):
    print(sequence[i])
    print(i)

#ked mam napisanu sequenci ako string viem indexovat ale nebudu nam fungovat metody z biopythonu

#indexace sequence
for i in range(len(sequence)):
    print(sequence[i])
    print(i)


########################################################################################################################
########################################################################################################################

from Bio.Seq import Seq

seq = Seq('ATGCCGTACG')
print(seq[0:3]) # treti sa nezahrna
print(seq[0:2])
print(seq[0])
print(seq[-1])
print(seq[4:10])
print(seq[2:9])

# opacne sequence
print(seq[::-1])
print(seq[:])

# indexacia od zaciatku po 5. prvok
print(seq[0:5])
print(seq[:5])
print(seq[5:])
print(seq[:5:2])

print(seq[::2])

print(seq[-5:-2])

print(seq[-2:-5:-1])

########################################################################################################################
########################################################################################################################

from Bio.Seq import Seq

seq = Seq('ATAGATCGATGCACCGAT')
seq2 = Seq('AAT')
seq3 = Seq('TGCATGCA')

#spojenie seq
seq_merged = seq + seq2 + seq3
print(seq_merged)

seq_merged2 = Seq('').join([seq, seq2, seq3])
print(seq_merged2)


#zmena velkosti
seq = Seq('ATGCgccaTCG')
seq.upper()
print(seq.upper())
print(seq.lower())

#pocitani bazi
seq = Seq('ATGCCCGATCGA')
num_of_a = seq.count('A')
print(num_of_a)

print()
print(seq)
print(seq.count('A', 7)) # od pate pozice pocitam dal
print(seq.count('A', 0, 8)) #tretia pozicia nie je zahrnuta teda 2

print()
#vyhledavani
seq = Seq('ATGCGCGCTACGATGC')
print(seq.find('TAC')) #vyhodi index pozicie prveho vyskytu
print(seq.find('f')) # ak sa to tam nenachcadza tak -1 vyhodi

########################################################################################################################
########################################################################################################################

from Bio.Seq import Seq

seq = Seq('ATGCGCGAGCGCTAGCATCGATAACGA')
mrna = seq.transcribe() #transkripce
print(mrna)
protein = mrna.translate() #translace
print(protein) #ked mi to hodi error tak to znamena ze sequence nie je delitelna 3

#translate sa da volat aj na dna a dostanem tu istu protein seq
print(seq.translate())


#iupac kod 1,2, 11 zapamatat cisla
#seq.translate(table = '2')
print(seq.translate(table = '11'))

