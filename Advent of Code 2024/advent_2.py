#!/usr/bin/env python3

# Advent 2

from util import read_input

levels_grid_raw = read_input("C:/Users/fdudi/OneDrive/Desktop/PythonHomework/rosalind_data/advent2.txt")

levels_grid = [[int(x) for x in line.split()] for line in levels_grid_raw]

# print(levels_grid)
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
          # step 1: what is the absolute difference?
          absol_dif = abs(number - level[i + 1])
          within_bounds = absol_dif < 4 and absol_dif > 0
          # step 2: is it monotonically falling/rising?
          if i != 0:
            is_between = (level[i - 1] < number and number < level[i + 1]) or (level[i - 1] > number and number > level[i + 1])
          else: 
            is_between = True

          # actually check the conditions
          if not within_bounds or not is_between:
              # unsafe_counter += 1
              break
        else:
            # print(level)
            safe_counter += 1 

print("There are", safe_counter, "safe levels")
# print("There are", unsafe_counter, "unsafe levels")