from Bio import SeqIO
from Bio.Align import sam
from Bio.Seq import MutableSeq, Seq
from Bio.SeqRecord import  SeqRecord

def get_sequence_with_quality(name_file, index_read):
    records = list(SeqIO.parse(name_file, 'fastq'))
    #print(len(records))
    if index_read > len(records):
        return 'index out of range'

    seq = MutableSeq(records[index_read].seq)
    phred = records[index_read].letter_annotations['phred_quality']

    for i in range(len(phred)):
        if phred[i] < 30:
            seq[i] = seq[i].lower()

    # v jednom riadku
    new_record = SeqRecord(seq, id=records[index_read].id, description='index_read')

    # ulozenie zaznamu alebo viac zaznamov pomocou seqIO
    final = SeqIO.write(new_record, handle='ukol_1.fasta', format='fasta')  # iba seqrecord objekty


    return final


x = get_sequence_with_quality('run1_R1.fq', 50)
print(x)