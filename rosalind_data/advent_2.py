#!/usr/bin/env python3

# Advent 2

from util import read_input

levels_grid_raw = read_input("C:/PythonHomework/rosalind_data/advent2.txt")

levels_grid = [[int(x) for x in line.split()] for line in levels_grid_raw]

print(levels_grid)
# example_levels = [
# [7, 6, 4, 2, 1],
# [1, 2, 7, 8, 9],
# [9, 7, 6, 2, 1],
# [1, 3, 2, 4, 5],
# [8, 6, 4, 4, 1],
# [1, 3, 6, 7, 9]]

safe_counter = 0
# unsafe_counter = 0

for level in levels_grid:
    for i, number in enumerate(level):
        # print(f"Number is {number} Index is {i}")
        if i + 1 < len(level):
          if i != 0:
            is_between = (level[i - 1] < number and number < level[i + 1]) or (level[i - 1] > number and number > level[i + 1])
            absol_dif = abs(number - level[i + 1])
            if absol_dif == 0 or absol_dif > 3 or not is_between:
                # unsafe_counter += 1
                break
        else:
            safe_counter += 1 

print("There are", safe_counter, "safe levels")
# print("There are", unsafe_counter, "unsafe levels")