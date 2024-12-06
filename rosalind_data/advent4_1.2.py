#!/usr/bin/env python

# Advent Day 4

from util import read_input

xmas_crossword = read_input("C:/PythonHomework/rosalind_data/advent_text.txt")

expected_string = "MAS"



def check_diagonally(y, x):
    number_matched = 0
    
    # diagonally to the bottom right for MAS
    if (
        x - 1 >= 0
        and y - 1 >= 0
        and x + 1 < len(xmas_crossword[y])
        and y + 1 < len(xmas_crossword)
    ):
        value_normal = (
            xmas_crossword[y - 1][x - 1]
            + xmas_crossword[y][x]
            + xmas_crossword[y + 1][x + 1]
        )
        if value_normal == expected_string or value_normal == expected_string[::-1]:
            number_matched += 1

    if (
        y - 1 >= 0
        and x + 1 < len(xmas_crossword[y])
        and y + 1 < len(xmas_crossword)
        and x - 1 >= 0
    ):
        value_normal = (
            xmas_crossword[y - 1][x + 1]
            + xmas_crossword[y][x]
            + xmas_crossword[y + 1][x - 1]
        )
        if value_normal == expected_string or value_normal == expected_string[::-1]:
            number_matched += 1
    if number_matched == 2:
        return 1
    else:
        return 0 


found_count = 0

for y in range(0, len(xmas_crossword)):
    for x in range(0, len(xmas_crossword[y])):
        if xmas_crossword[y][x] == "A":
          
            found_count += check_diagonally(y, x)


print(found_count)
