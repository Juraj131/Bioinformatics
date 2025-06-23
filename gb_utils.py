#sipka v ncbi ukazuje ci je komplementarne alebo originale sipka doprava je original

from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from Bio import SeqIO

#1 zaznam v tom co som si stiahol tak pouzijem read

fasta_record = SeqIO.read(handle='sequence1.fasta', format='fasta')

#zaznam v gb
gb_record = SeqIO.read(handle="sequence2.gb", format="genbank")
#print(gb_record.seq)
seq_homo = gb_record.seq

#dolezite features
#print(gb_record.features)
#print('')
#print(gb_record.features[3]) #indexace cez features

#print(len(gb_record.features)) # dlzka anotovanych oblasti

#print(gb_record.features[3].type) # takto zistim akeho typu je ficura
print(gb_record.features[3].location) #vlezem do souradnic ficury
print()
print(gb_record.features[3].location.parts) #location.parts[i] mam indexy exonu i
print(len(gb_record.features[3].location.parts))
print()
print(gb_record.features[3].location.parts[0].start) #start ukazuje od akej pozicie to zacina
print(gb_record.features[3].location.parts[0].end) #dostanem kde exon konci

#cds spajanie exonov a translatovnaie do proteinu
print(seq_homo[27710:27768].translate(table=1))

print(gb_record.features[3].qualifiers['translation']) #

print(gb_record.features[3].location.strand) #na akom vlajkne je gen kodovany ked je 1 tak je to veduce vlaknoa ked je -1 tak komplementarne

#ked prekladame z komplementarneho tak zoberieme exon urobim si z toho komplementarne vlakno a urobim z toho reverzny komplement a az potom prekladam do proteinov



# nacitanie viacerych sekvencii
#neda sa nacitavat cez read
record = list(SeqIO.parse(handle='3seq.fasta', format='fasta')) #treba ulozit aj do listu aby sa to dalo otvorit
print(record) # vsetky ti sekvencie
print(record[0]) # indexovanie jednotlivych sekvencii

# da sa prechadzat aj cez for cyklus
for record in SeqIO.parse(handle='3seq.fasta', format='fasta'):
     print(record.id)