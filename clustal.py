from Bio import AlignIO

aln_example = AlignIO.read('clustal_hemoglobin.aln-fasta','fasta')
print(aln_example)
print(format(aln_example, 'fasta')) #toto sluzi na zobrazovanie v roznych formatoch
print(format(aln_example, 'clustal'))

print(len(aln_example)) #zistenei poctu zarovnani
print(aln_example[0]) #indexovanie
#je to seqrecord takze vieme zistit seq a pod
print(aln_example[0].seq)

#zobrazenie prvniho sloupce resp ze ake su nukleotidy vo vsetktych zarovnaniach na prvej pozicii
print(aln_example[:,0])


#############################################################################################
#############################################################################################


# E value znamena ze aka je pravdepodobnost ze sa najde nahodna sekvencia ako ta nasa
#vsimame si total a max score e value a per indent
# totoal a max musi byt maximalna e value co najmensie a per indent cim viac percent tym viac sa podoba ta homologna sekvence na tu nasi
from Bio import AlignIO

aln_example = AlignIO.read('clustal_seqdump.aln-fasta','fasta')
print(aln_example)
print(format(aln_example, 'fasta')) #toto sluzi na zobrazovanie v roznych formatoch
print(format(aln_example, 'clustal'))

print(len(aln_example)) #zistenei poctu zarovnani
print(aln_example[0]) #indexovanie
#je to seqrecord takze vieme zistit seq a pod
print(aln_example[0].seq)

#zobrazenie prvniho sloupce resp ze ake su nukleotidy vo vsetktych zarovnaniach na prvej pozicii
print(aln_example[:,0])
