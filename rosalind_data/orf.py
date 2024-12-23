#!/usr/bin/env python3

# codon dictionary from prot.py


# used code from the REVC exercise to get the complementary strands
DNA_strand = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
reverse = DNA_strand[::-1]
complementary_nukes = str.maketrans("ATCG", "TAGC")
ComplementaryDNA = reverse.translate(reverse)
print(ComplementaryDNA)

code = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

start_codon = "AUG"
stop_codon = ("UAA", "UAG", "UGA")

ComplementaryDNA = "GATCTTGCCGTATCAGCAGTAGATAGCTCCAAAGAAGCTCCCTACGGCAGGCCGCGATAAGAGAACGTTCACAAGGAAAAACGCTAGAAATCAAGCAAGCCCGCGCTTGAAAGGCAGGACTGATTCCGGTAGAGGTGGTGGAGGGATCCTACGAACCCGGAACTCCCCCAAGTACCTTTGAGGTTGGCCGCGCAGCTCGTTATAGATCCGGCTTGAGTTTTAGTGTACTAAAGCATCCTACCTAACCCCTACGAATTGTGCTATGGATCCGTCGCAACCTATGCTCCTGCCATCGGGCAAACGGGTTGTTAGGGGCGTTACTACCAGCGACATAGACCAGCAAGCTGATAAGATTAAACCGTATCTGCTCCGACCCGCTCAGACACGGAACTTCGAACTAGTAGTACTCTTCCTCTCGGACCTTCCTGATAAGCGGGATGATTTCGGACGTGATAACAACTGGCGCTTAGCTAAGCGCCAGTTGTTATCACGTCCGAAATCATTTTTCCTACCAGTTTAGCACCTCAGTCGTCGCGACACAGCACGCTGAGTCCATAATCAACACCGGCCAAGCTTTACGGGATTCCGGTCCCGAGCAGCCTGGTCCGATTTCGCCCACGCCCTAATCACTGTCACCATCCCACGGACGAGCGTTCAAATTGACTTCCGGACTGAGTAAAAAGGCGGATCATTTCATTCTATGAAAACCTGCTTATGTCTGTCGGGCCGTCTTTCATATAGTTGGAACTAGGCGACTTCTGAGCACCATTGTATATCGCACTAGTGCTTATCTATAGTTGAGTCGCGCTGATCTGCCAGGTTCAATCACATCACGCTACAGCCACGCGGCCATGGTTAAGTCAGTCAAGAATAACCACGCAGGCCTCTCGGCACACGACTTTCGCCCTGGCGGTTATGGACTATCGGCGACTCACCTAAT"
DNA_strand = "ATTAGGTGAGTCGCCGATAGTCCATAACCGCCAGGGCGAAAGTCGTGTGCCGAGAGGCCTGCGTGGTTATTCTTGACTGACTTAACCATGGCCGCGTGGCTGTAGCGTGATGTGATTGAACCTGGCAGATCAGCGCGACTCAACTATAGATAAGCACTAGTGCGATATACAATGGTGCTCAGAAGTCGCCTAGTTCCAACTATATGAAAGACGGCCCGACAGACATAAGCAGGTTTTCATAGAATGAAATGATCCGCCTTTTTACTCAGTCCGGAAGTCAATTTGAACGCTCGTCCGTGGGATGGTGACAGTGATTAGGGCGTGGGCGAAATCGGACCAGGCTGCTCGGGACCGGAATCCCGTAAAGCTTGGCCGGTGTTGATTATGGACTCAGCGTGCTGTGTCGCGACGACTGAGGTGCTAAACTGGTAGGAAAAATGATTTCGGACGTGATAACAACTGGCGCTTAGCTAAGCGCCAGTTGTTATCACGTCCGAAATCATCCCGCTTATCAGGAAGGTCCGAGAGGAAGAGTACTACTAGTTCGAAGTTCCGTGTCTGAGCGGGTCGGAGCAGATACGGTTTAATCTTATCAGCTTGCTGGTCTATGTCGCTGGTAGTAACGCCCCTAACAACCCGTTTGCCCGATGGCAGGAGCATAGGTTGCGACGGATCCATAGCACAATTCGTAGGGGTTAGGTAGGATGCTTTAGTACACTAAAACTCAAGCCGGATCTATAACGAGCTGCGCGGCCAACCTCAAAGGTACTTGGGGGAGTTCCGGGTTCGTAGGATCCCTCCACCACCTCTACCGGAATCAGTCCTGCCTTTCAAGCGCGGGCTTGCTTGATTTCTAGCGTTTTTCCTTGTGAACGTTCTCTTATCGCGGCCTGCCGTAGGGAGCTTCTTTGGAGCTATCTACTGCTGATACGGCAAGATC"

peptides = []
for DNA in (ComplementaryDNA, DNA_strand):
    RNA = DNA.replace("T", "U")
    for start in range(0, len(RNA), 1):
        codon = RNA[start:start + 3]
        if codon == start_codon:
            peptide = ""
            for stop in range(start, len(RNA), 3):
                codon = RNA[stop:stop + 3]
                if codon in stop_codon:
                    if not peptide in peptides:
                        peptides.append(peptide)
                    break
                peptide += code[codon]

for peptide in peptides:
    print(peptide)
