#!/usr/bin/env

# 3. Check if All Numbers in a Sublist are Even

# Task:
# Given a list of lists, check if all numbers in any sublist are even.
# Return True if all numbers in the sublist are even, otherwise return False.

number_list = [[1,2,4,5,5,5],[4,4,2,2,3,1],[5,76,12,52,64],[23,15,643,1,123],[123,123,6,6,2,2,3,4],[1,6,87,3,5,1,23,5,6]]

for sublist in number_list:
    for numbers in sublist:
        if (numbers % 2) == 0:
            return True
    return False


        