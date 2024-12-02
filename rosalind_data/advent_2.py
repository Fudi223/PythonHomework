#!/usr/bin/env

# Advent 2

from util import read_input    

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

print(filepath)

# for numbers in range(len(levels) - 1):
#     if levels[numbers] > levels[numbers +1]:
#         print("Safe")
# for numbers in range(len(levels) - 1):
#     if levels[numbers] < levels[numbers +1]:
#         print("Safe")
# else:
#     print("Unsafe")

