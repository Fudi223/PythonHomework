#!/usr/bin/evn python

# 2. Find the Sum of All Numbers in a List of Lists
# Task:
# Given a list of lists of numbers, write a function that calculates the sum of all the numbers across all sublists.

number_list = [[1,2,4,5,5,5],[4,4,2,2,3,1],[5,76,12,52,64],[23,15,643,1,123],[123,123,6,6,2,2,3,4],[1,6,87,3,5,1,23,5,6]]

total_sum = 0

for sublist in number_list:
    for number in sublist:
        total_sum += number

print(total_sum)