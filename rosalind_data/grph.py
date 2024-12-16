#!/usr/bin/env python

# grph

strand_nr = ["Rosalind_0498", "Rosalind_2391", "Rosalind_2323", "Rosalind_0442", "Rosalind_5013"]
sequence = ["AAATAAA","TTTTCCC","AAATCCC", "GGGTGGG","AAATTTT"]

pairs = ""

# print(sequence[0],sequence[1])

def comparing_seqs():
    pairs = ""
    for i, j in enumerate(sequence):
        for k in j:
            if k[0:3][i] == k[0:3:-1][i+1]:
             pairs += j
    print(pairs)