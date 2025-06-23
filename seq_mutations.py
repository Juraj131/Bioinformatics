# Import necessary modules from Biopython
from Bio import SeqIO
from Bio.Align import sam
from Bio.Seq import MutableSeq, Seq
from Bio.SeqRecord import SeqRecord

def find_differences(name_fasta1, name_fasta2):
    # Read the first FASTA file
    record1 = SeqIO.read(name_fasta1, 'fasta')
    # Read the second FASTA file
    record2 = SeqIO.read(name_fasta2, 'fasta')
    # Get the length of the first sequence
    length_record1 = len(record1)
    # Get the length of the second sequence
    length_record2 = len(record2)

    # Check if the lengths of the sequences are different
    if length_record1 != length_record2:
        # If the first sequence is longer, set a warning message
        if length_record1 > length_record2:
            warning = f"Length is not the same: {length_record1} > {length_record2}"
        # If the second sequence is longer, set a warning message
        else:
            warning = f"Length is not the same: {length_record1} < {length_record2}"
        # Return the warning message
        return warning
    
    # Initialize lists to store differences
    list_index_differences = []
    list_nucleotide_diff_record1 = []
    list_nucleotide_diff_record2 = []
    # Iterate over the sequences to find differences
    for i in range(len(record1.seq)):
        # If nucleotides at the same position are different
        if record1.seq[i] != record2.seq[i]:
            # Append the index of the difference
            list_index_differences.append(i)
            # Append the differing nucleotide from the first sequence
            list_nucleotide_diff_record1.append(record1.seq[i])
            # Append the differing nucleotide from the second sequence
            list_nucleotide_diff_record2.append(record2.seq[i])

    # Return the lists of differences
    return list_index_differences, list_nucleotide_diff_record1, list_nucleotide_diff_record2

# Call the function with two FASTA files and print the result
x = differences = find_differences('reference_seq.fasta','run1_consensus.fa')
print(x)