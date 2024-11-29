#!/usr/bin/env python3

# codon dictionary from prot.py

code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

# used code from the REVC exercise to get the complementary strands

# dna_strand = "strand"
# reverse_strand = dna_strand[::-1]
# complementary_nukes = str.maketrans("ATCG", "TAGC")
# complementary_strand = reverse_strand.translate(complementary_nukes)
# print(complementary_strand)

# Here we can swap the "T" and "U" in both strands
ComplementaryDNA = "CTGAGATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGAGTTAGCTACATGGCT"
ComplementaryRNA = ComplementaryDNA.replace("T", "U")
DNA_strand = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
RNA_strand = DNA_strand.replace("T", "U")

# Here are our start and stop codons

start_codon = "AUG"
stop_codon = ("UAA", "UAG", "UGA")

# And from here on, I had help and unfortunately wasnt taken step by step so I am a little lost as to how the loops influence each other... 
# All seems very familiar from previous exercises, and while brainstorming, we got to how it needs to be solved, but not how to do the loops
# This worked out with the samples
# What is missing is the import and formatting of the rosalind files, like this it needs manual copy pasting
# I really want to know, how the nested loops here work...

peptides = list()

for RNA_trip in (ComplementaryRNA, RNA_strand):
    for start in range(0, len(RNA_trip), 1):
        codon = RNA_trip[start:start + 3]
        if codon == start_codon:
            peptide = ""
            for stop in range (start, len(RNA_trip), 3):
                codon = RNA_trip[stop:stop +3 ] 
                if codon in stop_codon:
                    if not peptide in peptides:
                        peptides.append(peptide)
                    break
                peptide += code[codon]
for peptide in peptides:
    print(peptide)