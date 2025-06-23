#konsenzulani sekvence: mame zarovnane sekvence a na danej pozicii berieme najviac zastupeny znak
from Bio import AlignIO
from collections import Counter
from Bio.Seq import Seq
from Bio.SeqRecord import  SeqRecord
from Bio import SeqIO

def get_consensus_from_alignment(input_fasta, output_fasta, nazev_fasta):
    aligned_seq = AlignIO.read(input_fasta, 'fasta')
    consensus = ''
    for i in range(len(aligned_seq[0].seq)): #vsertky seq su zarovnane takze su rovnako dlhe
        seq_column = aligned_seq[:,i]
        znak = Counter(seq_column).most_common(1)[0][0]
        consensus += znak

    new_record = SeqRecord(Seq(consensus),id=nazev_fasta)

    # ulozenie zaznamu alebo viac zaznamov pomocou seqIO
    SeqIO.write(new_record, handle=output_fasta, format='fasta')  # iba seqrecord objekty

#######################################
get_consensus_from_alignment('clustal_seqdump.aln-fasta', 'consensus_seq.fasta', 'consensus_seq')