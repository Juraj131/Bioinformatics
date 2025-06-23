import numpy as np
from Bio import Align
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from tqdm import tqdm



def ATB_resistance(pac_file, bak_file):
    pacienti = list(SeqIO.parse(pac_file, 'fasta'))
    bakteria = SeqIO.read(bak_file, 'fasta')

    seq_bak = bakteria.seq
    AA_seq_bak = seq_bak.translate(table=11)

    AA_seq_pacienti = []
    names_pacienti = []

    pacienti_atb = []
    pacienti_rezist = []
    for i in range(len(pacienti)):
        seq_pac = pacienti[i].seq
        name_pac = pacienti[i].id
        AA_seq_pac = seq_pac.translate(table=11)
        AA_seq_pacienti.append(AA_seq_pac)
        names_pacienti.append(name_pac)
        #if len(AA_seq_pac) != len(AA_seq_bak): #kontrola ci mutacie substitucie
            #print(True)
        if AA_seq_pac == AA_seq_bak:
            pacienti_rezist.append(name_pac)
        else:
            for j in range(len(AA_seq_pac)):
                if AA_seq_bak[j] != AA_seq_pac[j]:
                    pacienti_atb.append(name_pac)
                    z = j * 3
                    changed_codon = seq_pac[z:z+3]
                    original_codon = seq_bak[z:z+3]
                    pacienti_atb.append(f'{original_codon}-->{changed_codon}')
                    #pacienti_atb.append(AA_seq_pac[j])

    return pacienti_atb, pacienti_rezist



############################################################################
x, y = ATB_resistance('samples_from_pacients.fasta', 'blaCTX-M.fasta')
print(x)
print(y)

    


