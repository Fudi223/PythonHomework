#!/usr/bin/env python3

# Advent 2


import os # Used for global same directory call to "safeornot.txt"

# Global call to safeornot.txt
here = os.path.dirname(os.path.abspath(__file__))
safeornot = os.path.join(here, "advent2.txt")


def is_valid_range(line):
  """Checks if a line representing a range of numbers has gaps <= 3."""

  numbers = [int(x) for x in line.split()] 

  if len(numbers) < 2:
    return False  # Not enough numbers to check

  is_ascending = numbers[1] > numbers[0]  # Determine initial direction  

  for i in range(1, len(numbers)):
    gap = abs(numbers[i] - numbers[i - 1])  # Calculate absolute gap
    if gap > 3:
      return False  # Gap too large

    if is_ascending and numbers[i] <= numbers[i-1]:
      return False  # Violated ascending order
    elif not is_ascending and numbers[i] >= numbers[i-1]:
      return False  # Violated descending order

  return True  # All checks passed

true_count = 0

with open(safeornot, "r") as file:
  for line in file:
    is_valid = is_valid_range(line.strip())
    print(f"Line '{line.strip()}': {is_valid}") 
    if is_valid:
        true_count += 1

print(true_count)

