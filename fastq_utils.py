from Bio import SeqIO

records = list(SeqIO.parse('run1_R1.fq', 'fastq'))


print(records[0]) #prvni cteni
print(len(records)) #pocet cteni

#for read in SeqIO.parse('run1_R1.fq', 'fastq'):
  #  print(read)

print(records[0].seq) #sekvence
print(records[0].id) #id
print(records[0].format('fastq')) #da sa na to pozriet ako na fastq alebo fasta

print(records[0].letter_annotations['phred_quality']) # uz rovno vypocita phred skore
