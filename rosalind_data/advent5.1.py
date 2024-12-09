#!/usr/bin/env python

# Advent 5

# Input: Pages for the safety manuals must be printed in a specific order:
# Notation x|y = if both page number x and y are to be produced as part of an update:
# Page number x must be printed before page number y
# Page ordering rules in each update are given, but it isnt given whether
# each update has the pages in right order. There can be numbers between
# the given rule numbers, as long as the order is ok.

# The middle page number is also required. The ones from the correctly-ordered pages
# need to be added up and submitted.


# Explanation: first rule is 47|53, and the first printed page is
# 75, 47, 61, 53, 29. This would be correct, because 47 comes before
# 53, as specified in the first rule.
# The fourth update is wrong, because the rule 97|75 was violated.
# fith and last are also not in the correct order.

from util import read_input

printed_pages = read_input(
    "C:/Users/fdudi/OneDrive/Desktop/PythonHomework/rosalind_data/advent5_input.txt"
)

rules_example = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13],
]



updates_examples = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

# Step 1: Compare EVERY LIST in updates to EVERY LIST in rules. Go over each number, whereas first it should be checking the rules lists content.
# Step 2: Rules list content goes over each number in the updates lists.
# Step 3: Create conditions (if the order is ok, keep the list and put it into a new one. if its not, skip it)
# Step 4: Find a way to take the middle number of each valid list and put it into its own list and then add em all together!
# Step 5: gg(?)
