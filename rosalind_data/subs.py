# # SUBS Exercise: Finding a Motif in DNA

# # Given are two DNA strings s and t

# # Return should be all locations of t as a substring of s!

# # Sample Dataset:


# # Sample output should be "2 4 10" (corresponding to the positions where "ATAT" occurs, specifically only the start position)

# # Similar to the HAMM, Zipping might work, however I need to figure out, how to read over patterns rather than single characters of a string. 
# # Slicing will also be essential, combined with printing out the starting position of "t". So, maybe writing a loop that 1. checks all the positions where "t" occurs will be needed. 
# # This should not be as much of a problem if I use part of the loop from HAMM, and 2. the output should be a string with the given positions where "t" starts.

# # The loop will first go over "s", find the first "t" quadruplet, get the number of the starting position, keep going, find the next "t" quadruplet, get the next number... etc.
# # until it went over the entire string "s". 

# # Since using zip() wouldnt put the whole "t" together with "s", but only single characters, it might be worth a try, to put "ATAT" into a dict and zip that with "s". 
# # The idea is that it takes the whole sequence. The tricky part left is to figure out, how to make the loop recognize the quadruples (or the pattern) of "s".


# I ended up checking out Ines solution, tried to understand how and why it works and adapted it. Its very clean, gotta say. Still not sure how to fix the problem with having to add characters

s = "TCTGCGCTCTGCGCTCTGCGCATCTGCGCTTTCGTCTGCGCATAAGTGGTAACGGTATCTGCGCATTCTGCGCATGAAAGTCGTTTTCTGCGCGTCTGCGCAGATCTGCGCATCTGCGCTTCTGCGCGAGATTCTGCGCTTAATTCTGCGCATCTGCGCTTCTGCGCGCATCTGCGCTCTGCGCATTCTGCGCATGCATCTGCGCTCTTGAGGCGTTCTGCGCTCTGCGCCTCTGCGCCGCAAGACTCTGCGCTCTGCGCAACCTTAACGTTCTGCGCTCATTCTGCGCTGCCTGATTCTGCGCTCTGCGCTCTGCGCTTCATTCTGCGCACTATGTCTCTGCGCTCTGCGCATTCTGCGCCTCTGCGCCTCTGCGCCATCTGCGCTTCTGCGCAAGGGCGTACCATGATCTGCGCTTCTGCGCAAGTTTTCTGCGCATCTGCGCGATCTGCGCTCTGCGCAGTCTGCGCCCCGCCATCATCTAGTCTGCGCTTCTGACTTCTGCGCATCTGCGCCCTCTGCGCTGTCTGCGCTCTGCGCTCTGCGCTCTGCGCGTCTGCGCGTCTGCGCATCTGCGCTCTGCGCGTGTCTGCGCGCTCTGCGCCTCTGCGCAGTTCTGCGCTTCTGCGCCTCTGCGCCGTCTGCGCTTCTGCGCAATGTTCTGCGCGGAATCTGCGCAACCTTCTGCGCTCTGCGCTCTGCGCGCTCTGCGCTGGTCTGCGCGCGTTCTGCGCTCTGCGCGGCGTCTGCGCGATCTGCGCATCTGCGCCCCGTAGCGAATTTTTCTGCGCTTCTGCGCAGCATTCTGCGCTCTGCGCTAAGTCTGCGCTCTGCGCATATCTGCGCGTCTGCGCTCTGCGCTAAAGTTATCTGCGCXXXXXXXXX"
t = "TCTGCGCTC"

positions = []

for pos_s, base_s in enumerate(s):
    for pos_t, base_t in enumerate(t):
        if s[pos_s + pos_t] != t[pos_t]:
            break
        if (pos_t + 1) == len(t):
            positions.append(pos_s + 1)
for a in positions:
    print(a, end=" ")
print()

