# SUBS Exercise: Finding a Motif in DNA

# Given are two DNA strings s and t

# Return should be all locations of t as a substring of s!

# Sample Dataset:

s = "GATATATGCATATACTT"
# t = "ATAT"

# Sample output should be "2 4 10" (corresponding to the positions where "ATAT" occurs, specifically only the start position)

# Similar to the HAMM, Zipping might work, however I need to figure out, how to read over patterns rather than single characters of a string. 
# Slicing will also be essential, combined with printing out the starting position of "t". So, maybe writing a loop that 1. checks all the positions where "t" occurs will be needed. 
# This should not be as much of a problem if I use part of the loop from HAMM, and 2. the output should be a string with the given positions where "t" starts.

# The loop will first go over "s", find the first "t" quadruplet, get the number of the starting position, keep going, find the next "t" quadruplet, get the next number... etc.
# until it went over the entire string "s". 

# Since using zip() wouldnt put the whole "t" together with "s", but only single characters, it might be worth a try, to put "ATAT" into a dict and zip that with "s". 
# The idea is that it takes the whole sequence. The tricky part left is to figure out, how to make the loop recognize the quadruples (or the pattern) of "s".

quad = {"t": "ATAT"}

#zip(s, quad["t"])

positions = ""

# Here I wanted to try using a nested loop. I got rather confused by the end so I moved on to other things. I just get 9 empty lines printed in bash, so its probably only counting the "Ts"

# for pos_s in zip(s, quad["t"]):
#     for spot in pos_s:
#         if pos_s == quad["t"]:
#             positions += pos_s[spot::]
#         print(positions)

# Other attempt: maybe I dont need a zip() at all? But all I get is just 18 empty lines in bash....

# for pos_s in s:
#     if s == quad["t"]:
#         positions += pos_s[::]
#     print(positions)