from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from Bio import SeqIO

#genbank je textovy format
#genbank ma hlacvicku: identifikator delka, dna rna, protein co to je za sekvenci z akeho organizmu z akej cast
# druha cast anotace: features rozneho typu... 1 source delka seqvence a z akeho je organizmu
# CDS kdoujici oblasti, oznaceni genu, poromotory a terminator ale hlavne obsahuje useky EXONOV
# mRNA v cds su uz exony a introny oblasti od 5UTR do 3UTR
#gen> oblast genu a kde je pormotor , cast neprekladaneho useku a exony introny, co sa nepreklada konec sekvence a terminator



seq = Seq('ATGCTGACTACG')

sequence = SeqRecord(Seq('ATGCATGCTAGC')) # do seqrecord sa uz musi zadavat sekvencia triedy seq
print(sequence)

#atributy
print(sequence.id) # viem indexovat atributy v mojom zazname

#ulozenie atributu
sequence.id = 'ID1'
sequence.name = 'hello'
print(sequence)

print(sequence.seq) #takto sa dostanem k tej sekvencii

# v jednom riadku
new_record = SeqRecord(Seq('ATGGC'), id='akfm', description='fagfgs')

# ulozenie zaznamu alebo viac zaznamov pomocou seqIO
list_record = [sequence, new_record]
SeqIO.write(list_record, handle='moje_sekvence.fasta', format='fasta') #iba seqrecord objekty



