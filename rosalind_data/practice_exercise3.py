#!/usr/bin/env

# 3. Check if All Numbers in a Sublist are Even

# Task:
# Given a list of lists, check if all numbers in any sublist are even.
# Return True if all numbers in the sublist are even, otherwise return False.

number_list = [[1,2,4,5,5,5],[4,4,2,2,3,1],[2,76,12,52,64],[23,15,643,1,123],[123,123,6,6,2,2,3,4],[1,6,87,3,5,1,23,5,6]]


def even(number_list):
    for sublist in number_list:
        all_is_even = (numbers % 2 == 0 for numbers in sublist):

            
print(even(number_list))