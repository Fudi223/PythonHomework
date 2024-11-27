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

s= "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
t = s.replace("T", "U")
       
print(t)


# positions = []

# for pos_s, base_s in enumerate(s):
#     for pos_t, base_t in enumerate(t):
#         if s[pos_s + pos_t] != t[pos_t]:
#             break
#         if (pos_t + 1) == len(t):
#             positions.append(pos_s + 1)
# for a in positions:
#     print(a, end=" ")
# print(s)


# # read triplets

# rna = string[0]

# # read the rna in triplets:
# peptide = ""
# for start in range(0, len(rna), 3):
#     codon = rna[start:start+3]
#     aminoacid = code[codon]
#     if aminoacid == "Stop":
#         break
#     peptide += aminoacid
#     # print(codon, "corresponds to", aminoacid)

# print(peptide)