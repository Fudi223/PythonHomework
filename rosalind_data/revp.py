#!usr/bin/env python

# Rosalind REVP

sample = "TCAATGCATGCGGGTCTATATGCAT"

# takes a string as an input, reverses it and then creates the complementary strand by replacing ATGC with TACG.
# def strand_complementing(file):    
#     sample_reversed = file[::-1]
#     sample_complemented = ""
#     for base in sample_reversed:
#         if base == "A":
#             sample_complemented += "T"
#         if base == "T":
#             sample_complemented += "A"
#         if base == "G":
#             sample_complemented += "C"
#         if base == "C":
#             sample_complemented += "G"
#     return sample_complemented

# next, figure out how to read the string and find the palindromes:

# Start with reading the first letter, then check the string until we find the complementary base
# after we find that, we check the next letter after the first one has its complementary base one position before the complementary base of the first one
# that would be put like this, for the sample: t = sample[0:], a = sample [2:]. then the next letter is c. c = sample[t+1:]. so to check if it has a complementary base before a : 
# it would look have to go -1 from the position of a, so sample[a-1:]. Here however, it would be a c, not to mention that there if there arent more than 2 letters inbetween the start and last
# position, it cant be a palindrome. Then we repeat the process for the next position in the string and so on. The ending border has to be defined, so we dont go outside of it.
# it would be put like so : range(0, len(sample) - 1) (I think). So now we can find the palindromes (hopefully). Next, we will need the starting position of them in the sample string and
# their lenght. Lets start with the first one. To get the starting position, we need to set a condition, that will put the number of the position into either a list, or an empty string, or maybe 
# even a dictionary (key = position; value = lenght). But putting them into a string might be probably easier at first. How? The condition can be implemented and set at the point in the loop,
# where it is identified as valid in the first place. for that, we can use an if statement (somehow. Ill cross that bridge when I get to it.). The lenght shouldnt be too difficult. Once the
# palindrome has been found, we need to add the len(palindrome) integer to our results string, so results_len += len(palindrome). And that should be it! (I hope).
# Note: make sure to search in a range of 12 and in the whole range so that a potential palindrome wont be overlooked and not checked.

for i, x in enumerate(sample):
    