#!/usr/bin/env python

# PROT Exercise

# Given: An RNA string "rosalind_prot" corresponding to a strand of mRNA (of lenght at most 10kbp)

# Return: The protein string encoded by "rosalind_prot"

# First, lets use the read_input function from the util list

# Second, create dictionary including the RNA codon table

# Third, figure out a way to read every 3 characters in "rosalind_prot", while checking the dictionary for the corresponding key, and then replacing it with the value

# Fourth, save the new string with the values corresponding to their keys (or nucleotide triplets) in a new list "protein_string" and print it

# Thoughts: I'd like to try and seperate the string after every 3rd step. There might be a way to do it with slicing maybe?
# Findings Nr1: Ok so after some research online, I managed to get a loop together to slice the sequence into triplets, however, its not working with the read_input function?
# When I use the read_input function, print(len(sample_stringtext)) gives me the number "1", however it should be 51! Why is that happening? Is there something wrong with how
# the util file works? If this gets fixed, then I think I can continue with solving the next steps (hopefully)...

# Go over the input, don't modify it!

from util import read_input

sample_stringtext = read_input('./rosalind_prot.txt')

sequence_string = sample_stringtext[0]

codon_table_dict = {
"UUU": "F", "CUU": "L", "AUU": "I","GUU": "V",
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
"UGA": "Stop", "CGA": "R","AGA": "R", "GGA": "G",
"UGG": "W", "CGG": "R","AGG": "R", "GGG": "G"}

# print(codon_table_dict["AAA"])

# print(len(sample_stringtext))

# Note: using read_input from util is not working for some reason, the lenght for the sample_stringtext appears to be "1", which is not the case (it should be 51).
# -> SOLUTION: the input file has to be assigned to a new variable that looks like this: "list_new = read_input(./sample.txt)   string = list_new[0]". This way, the whole text (or string)
# isn't read as just one element, because its a list otherwise

# for prots in codon_table_dict:
#     if prots == codon_table_dict["AUG"]:
#         print(codon_table_dict.values)
#     else:
#         print("not found")

# I tried it with defining a new variable with the example code from Rosalind, and this worked the way it should! It counted the lenght right, and it managed to slice it into triplets.

sequence = sequence_string

for start_of_sequence in range(0, len(sequence), 3):
    print(sequence[start_of_sequence:start_of_sequence+3])
    codon = sequence[start_of_sequence:start_of_sequence+3]
    if len(codon) == 3:
        print(codon)



