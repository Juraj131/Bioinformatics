from Bio import SeqIO
from Bio.Align import sam
from Bio.Seq import MutableSeq, Seq
from Bio.SeqRecord import  SeqRecord

def get_information_about_assembly(name_reference_seq, name_assembly_seq):
    # budem musiet prechadzat list ktory obsahuje sam soubory  a to bude namiesto name assembly

    #nacteni ve fasta formatu
    record = SeqIO.read(name_reference_seq, 'fasta')

    #zistenie delky sekvence
    n_ref_seq = len(record.seq)
    print(f'Dĺžka referenčnej sekvencie je: {n_ref_seq}')

    #prechadzanie sam suborov
    for i in range(len(name_assembly_seq)):
        with open(name_assembly_seq[i], 'r') as sam_file:  # mapovanie cteni
            alignments = sam.AlignmentIterator(sam_file)

            #zistit sekvenciu cteni
            list_of_align_reads = []
            for align_read in alignments:
                list_of_align_reads.append(align_read) #toto je list v ktorom su vsetky citania vybraneho sam suboru
            
            sum_length_reads = 0
            for j in range(len(list_of_align_reads)):
                sum_length_reads += len(list_of_align_reads[j].query.seq)
            #teraz by sm mal vypocitat coverage ako nasobok dlzky daneho citania a priemerneho citania v sam subore a vydelit dlzkou referencneho genomu
            n_reads = len(list_of_align_reads)
            average_length_reads = sum_length_reads / n_reads
            average_coverage = (n_reads * average_length_reads) / (n_ref_seq)
            print(f'Priemerná dĺžka čítania je: {average_length_reads}')
            print(f'Priemerná coverage je: {average_coverage}')

get_information_about_assembly('reference_seq.fasta', ["run1_bwa.sam","run2_bwa.sam"])
