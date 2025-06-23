from Bio.Align import sam

with open('run1_bwa.sam', 'r') as sam_file: #mapovanie cteni
    alignments = sam.AlignmentIterator(sam_file)
    print(alignments)

    print(len(alignments)) #kolko mam v sam souboru namapovanych cteni



    list_of_align_reads = []
    for align_reads in alignments:
        #print(align_reads) # vo vrchny castui printu je referencna sekvence a v spodnej je namapovana
        list_of_align_reads.append(align_reads)

    print(list_of_align_reads[0]) # len jedno cteni
    print(list_of_align_reads[0].query.seq) #dostanme s ak sekvenci cteni, takto sa dostanme k sekvenci
    print(len(list_of_align_reads[0].query.seq)) #ako je to cteni dlhe, cez .seq sa dostaneme priamo kk tej sekvencii