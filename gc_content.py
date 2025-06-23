from matplotlib import pyplot as plt

import numpy as np
from Bio import Align
from Bio import SeqIO

def plot_GC_content(filenames, window_size):
    for filename in filenames: #prechadzam vstky nazvy fasta suborov
        record = SeqIO.read(filename, 'fasta') #otvaram fasta subor
        seq = record.seq #ziskavam sekvenciu

        position = [] #vytvorenie pozicii
        GC_percent = [] #vytvorenie listu kde sa budu ukladat percenta vyskytu G a C
        for i in range(len(seq) - window_size): #idem v sekvenciu po dlzku sekvencie okrem posledneho okna od konca aby nevznikol nulovy vyskyt
            subseq =  seq[i:i+window_size] #vytvaram okno
            G_content = subseq.count('G') #pocitam G v danom okne
            C_content = subseq.count('C') #Pocitam C v danom okne
            GC_content_perc = ((G_content + C_content) / window_size) * 100 #vypocet percent v danom okne
            position.append(i)  #ulozenie pozicie do listu
            GC_percent.append(GC_content_perc) #ulozenie percentualneho vyskytu GC v sekvencii don listu
    
        #vykreslenie grafu pre danu sekvenciu v danom subore fasta
        plt.plot(position, GC_percent) 
        plt.title(record.id)
        plt.xlabel("Pozice v sekvenci [bp]")
        plt.ylabel("GC obsah [%]")
        plt.tight_layout()
        plt.show()



###################################################################################################################
plot_GC_content(['AP017920.1.fasta','CP003131.1.fasta'], 1000)