#!usr/bin/env/python

# rosalind IPRB

# k = homozygotous dominant for a factor
# m are heterozygotous 
# n are homozygotous recessive

# Given: are individuals with positive integers with the characteristics abov
# Return Probability that two randomly selected mating organisms will produce an 
# individual possesing a dominant allele. Any two organisms can mate.

# From the sample dataset:

k = 20 #AA - homozygotous dominant 
m = 26 #Aa - heterozygotous
n = 22 #aa - homozygotous recessive

# Pr(offspring=dominant) - > offspring with Ax ->
# Pr(AA) + Pr(Aa)

# Output should be 0.78333

# Pop = 6 #(k+m+n)



# HoDom = k % Pop
# He = m % Pop
# HoRec = n % Pop
# Drawing random balls:
# X : draw a random ball, what is the colour?
# if there are 3 red balls and 2 blue balls, then Pr(X=red)=3/5 and Pr(X=Blue)=2/5
# Y would be drawing a second ball at random and it being blue.

def chances(k, m, n):
    Pop = k + m + n
    Pop1 = (k / Pop) + ((m / Pop) * ((4 * k + 3 * m - 3 + 2 * n) / (4 *(Pop - 1))) + (n / Pop) * ((2 * k) + m) / (2 * (Pop - 1)))
    return Pop1
print(chances(k, m, n))