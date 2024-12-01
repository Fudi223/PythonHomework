#!/usr/bin/env

# CONS exercise from Rosalind

# Needs: Make DNA strings matrix from imported FASTA file. The nr of rows = len(sequences), number of columns = nr of sequences from the fasta file.
# Count each occurences of the letters in columns, pick the one with the highest frequency and then print it in the profile matrix. Then take the
# Nucleotides with the highest number and print the corresponding letter. 

DNA_matrix = [[]]
Consensus_Matrix = [[]]

seqs = ["ATCCAGCT",
	    "GGGCAACT",
	    "ATGGATCT",
	    "AAGCAACC",
	    "TTGGAACT",
	    "ATGCCATT",
	    "ATGGCACT",]

nucleotide_counter = {"A": 0,
               "B": 0,
               "C": 0,
               "D": 0}
counter = " "

for s in range(0, len(seqs)):
    if (seqs[s] !="A"):
        counter = counter + 1
    if (seqs[s] !="T"):
        counter = counter + 1
    if (seqs[s] !="C"):
        counter = counter + 1
    if (seqs[s] !="G"):
        counter = counter + 1
print(str(counter))