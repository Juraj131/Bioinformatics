from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from Bio import SeqIO
def get_protein_sequences(input_name, output_name):
    records = list(SeqIO.parse(input_name, 'fasta'))
    records_prot_sequences = []
    for i in range(len(records)):
        records_prot_sequences.append(SeqRecord(Seq(records[i].seq.translate(table=2)), id=records[i].id, description=f'cytb_sample_{i+1}')) #cytb je mitochondrialny genom
    SeqIO.write(records_prot_sequences, output_name, 'fasta')
#######################
get_protein_sequences('cytb_set_seq.fasta','cytb_set_prot_seq.fasta')