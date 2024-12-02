#!/usr/bin/env

# 1st Advent exercise

list_a = ""
list_b = ""

list_a_sorted = sorted(list_a)
list_b_sorted = sorted(list_b)

print(list_a_sorted)
print(list_b_sorted)

list_difference = [abs(a - b) for a,b in zip(list_a_sorted, list_b_sorted)]

sum_differences = sum(list_difference)

print(sum_differences)