#!/usr/bin/env python3



months = int(input("How many months? "))
pairs = int(input("How many pairs? "))

n = months

k = pairs



# def rabbits(n,k):
#     if n < 1 : 
#         return 0
#     if n == 1 or n == 2:
#         return 2
#     return rabbits(n-1, k) + k * (n -2)

# print(rabbits(n,k))

def rabbits(n,k):
    if n < 2 : 
        return n
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)

print(rabbits(n,k))