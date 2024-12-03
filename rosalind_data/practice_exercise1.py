#!/usr/bin/env python

number_list = [1,2,4,5,5,5,4,4,2,2,3,1,5,76,12,52,64,23,15,643,1,123,123,123,6,6,2,2,3,4,1,6,87,3,5,1,23,5,6]


# print(number_list)
#1. Check if a Number Exists in a List of Lists
#Task:
#    Given a list of lists, check if a specific number exists in any of the sublists.
#    Return True if the number is found, otherwise return False.

searched_nr = 28282828

counter = 0 

def nr_check(number_list, searched_nr):
    for number in number_list:
        if number == searched_nr:
            return True
    return False

for nr_count in number_list:
    if nr_count == searched_nr:
        counter += 1

print(counter)
print(nr_check(number_list, searched_nr))