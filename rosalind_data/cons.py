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
               "T": 0,
               "G": 0,
               "C": 0}

for seq in seqs:
    for nucleotide in seq:
        if nucleotide in nucleotide_counter:
            nucleotide_counter[nucleotide] += 1
print(nucleotide_counter)

