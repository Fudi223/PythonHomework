#!/usr/bin/env python

# Advent Day 4

from util import read_input

xmas_crossword = read_input("C:/PythonHomework/rosalind_data/advent_text.txt")

expected_string = "XMAS"

def check_horizontal(y, x):
    number_matched = 0

    if x + 3 < len(xmas_crossword[y]):
        value_normal = (
            xmas_crossword[y][x]
            + xmas_crossword[y][x + 1]
            + xmas_crossword[y][x + 2]
            + xmas_crossword[y][x + 3]
        )
        if value_normal == expected_string:
            number_matched += 1

    if x - 3 >= 0:
        value_reverse = (
            xmas_crossword[y][x]
            + xmas_crossword[y][x - 1]
            + xmas_crossword[y][x - 2]
            + xmas_crossword[y][x - 3]
        )
        if value_reverse == expected_string:
            number_matched += 1

    return number_matched


def check_vertically(y, x):
    number_matched = 0

    if y + 3 < len(xmas_crossword):
        value_normal = (
            xmas_crossword[y][x]
            + xmas_crossword[y + 1][x]
            + xmas_crossword[y + 2][x]
            + xmas_crossword[y + 3][x]
        )
        if value_normal == expected_string:
            number_matched += 1

    if y - 3 >= 0:
        value_reverse = (
            xmas_crossword[y][x]
            + xmas_crossword[y - 1][x]
            + xmas_crossword[y - 2][x]
            + xmas_crossword[y - 3][x]
        )
        if value_reverse == expected_string:
            number_matched += 1

    return number_matched


def check_diagonally(y, x):
    number_matched = 0

    # diagonally to the bottom right
    if x + 3 < len(xmas_crossword[y]) and y + 3 < len(xmas_crossword):
        value_normal = (
            xmas_crossword[y][x]
            + xmas_crossword[y + 1][x + 1]
            + xmas_crossword[y + 2][x + 2]
            + xmas_crossword[y + 3][x + 3]
        )
        if value_normal == expected_string:
            number_matched += 1

    # diagonally to the top left
    if x - 3 >= 0 and y - 3 >= 0:
        value_reverse = (
            xmas_crossword[y][x]
            + xmas_crossword[y - 1][x - 1]
            + xmas_crossword[y - 2][x - 2]
            + xmas_crossword[y - 3][x - 3]
        )
        if value_reverse == expected_string:
            number_matched += 1

    # diagonally to the top right
    if x + 3 < len(xmas_crossword[y]) and y - 3 >= 0:
        value_normal = (
            xmas_crossword[y][x]
            + xmas_crossword[y - 1][x + 1]
            + xmas_crossword[y - 2][x + 2]
            + xmas_crossword[y - 3][x + 3]
        )
        if value_normal == expected_string:
            number_matched += 1

    # diagonally to the bottom left
    if x - 3 >= 0 and y + 3 < len(xmas_crossword):
        value_normal = (
            xmas_crossword[y][x]
            + xmas_crossword[y + 1][x - 1]
            + xmas_crossword[y + 2][x - 2]
            + xmas_crossword[y + 3][x - 3]
        )
        if value_normal == expected_string:
            number_matched += 1

    return number_matched


found_count = 0

for y in range(0, len(xmas_crossword)):
    for x in range(0, len(xmas_crossword[y])):
        if xmas_crossword[y][x] == "X":
            found_count += (
                check_horizontal(y, x) + check_vertically(y, x) + check_diagonally(y, x)
            )

print(found_count)
