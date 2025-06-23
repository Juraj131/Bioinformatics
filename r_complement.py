#from Bio.Seq import Seq
#seq = Seq('ATGCAGCAGCTAGCA')
#complement = seq.complement()
#print(complement)

#citame v smere 5 3 preto vytvarame reverzni komplement
#rcomplement = seq.reverse_complement()
#print(rcomplement)

def extract_subsequence(seq, start, end):
    subseq = seq[start:end]
    complement = []
    for i in range(len(subseq)): #pozor na chybu ked pouzivam len range tak tam mam index a nie konkretne pismeno
        if subseq[i] == 'A':
            complement.append('T')
        elif subseq[i] == 'T':
            complement.append('A')
        elif subseq[i] == 'C':
            complement.append('G')
        else:
            complement.append('C')
    rcomplement = complement[::-1]

    return complement, rcomplement

x = extract_subsequence('ATGCGCTACGTACGA', 0, 3)
print(x)

# Spojenie zoznamov do reťazcov
complement_str = ''.join(x[0])
rcomplement_str = ''.join(x[1])

# Spojenie oboch reťazcov do jedného súvislého reťazca
moj_string = complement_str + rcomplement_str
print(moj_string)

