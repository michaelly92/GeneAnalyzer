#!/usr/bin/env python
# coding: utf-8

# In[106]:


def get_gene_data(gene):
    
    gene_info = []
    
    for i in range(0, len(gene), 2):
        gene_name = gene[i]
        sequence = gene[i + 1] 
        gene_info.append((gene_name, sequence)) #group gene and sequence data together
        
    #some high integer
    shortest_gene = 1000
    shortest_length = 1000
    
    for gene_name, sequence in gene_info:
        exons = []
        introns = []
        exon_sequence = ''
        intron_sequence = ''
        exon_count = 0
        intron_count = 0
        
        # check if intron or exon
        for base in sequence:
            if base.isupper():
                exon_sequence += base
            else:
                intron_sequence += base
                
        #add exon until lowercase then add intron
        if exon_sequence:
            exons.append(exon_sequence)
            exon_count += 1
        
        if intron_sequence:
            introns.append(intron_sequence)
            intron_count += 1
        
        if len(sequence) < shortest_length:
            shortest_gene = gene_name
            shortest_length = len(sequence)
            
        exon = ''.join(exons)
        intron = ''.join(introns)
        print("Gene: " , gene_name)
        print("Exons: ", exon)
        print("Introns: ", intron)
        print("Gene Length: ", len(sequence))
        print("Total Exon Length: ", len(exon))
        print("Number of Exons: ", exon_count )
        print("Total Intron Length:" ,len(intron))
        print("Number of Introns:" , intron_count)
        print("---------------------------")
    
    print("shortest gene sequence is: " , shortest_gene)
    
    
with open("genes.fa" , 'r') as file:
    dna_data = file.read().splitlines()

#removes > operator from file
delete = '>'
new_dna_data= []
for element in dna_data:
    temp = ""
    for ch in element:
        if ch not in delete:
            temp += ch
    new_dna_data.append(temp)
#splits dna data into seperate gene data
#print(new_dna_data)
get_gene_data(new_dna_data)

input("Enter to exit")

