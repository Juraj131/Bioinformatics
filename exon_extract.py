from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from Bio import SeqIO

def get_proteins(record):
    record = SeqIO.read(handle=record, format='gb')
    seq = record.seq
    list_exon = []
    for i in range(0, len(record.features)):
        if record.features[i].type == 'CDS':
            if record.features[i].location.strand == 1: #veduce vlakno
                for j in range(0, len(record.features[i].location.parts)):
                    exon = seq[record.features[i].location.parts[j].start : record.features[i].location.parts[j].end]
                    list_exon.append(exon)

            else: #komplemetarne vlakno
                for z in range(0, len(record.features[i].location.parts)):
                    exon_complement = seq[record.features[i].location.parts[z].start : record.features[i].location.parts[z].end]
                    exon_complement.reverse_complement()
                    list_exon.append(exon_complement)

    # Konverzia každého prvku na reťazec a spojenie do jedného reťazca
    combined_sequence = Seq(''.join(str(exon) for exon in list_exon))
    #translacia
    protein_seq = combined_sequence.translate()
    #vytvorenie noveho zaznamu
    new_record = SeqRecord(protein_seq, id=record.id, description='fagfgs')
    
    # uloženie do FASTA súboru
    final_record = SeqIO.write(new_record, "output.fasta", "fasta")

    return final_record


# Príklad použitia funkcie
x = get_proteins('sequence2.gb')
                    

print(x)