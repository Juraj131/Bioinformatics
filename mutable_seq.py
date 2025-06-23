from Bio.Seq import MutableSeq, Seq

seq = Seq('ATGAT')
 #kebyze chcem prepisat tu sekvenci tak trieda Seq na to nebude fungovat na to sluzi mutable seq

seq2 = MutableSeq('ATATATA')
seq2[0] = 'a'

