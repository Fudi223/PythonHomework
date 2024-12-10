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

# from util import read_input

# printed_pages = read_input(
#     "C:/Users/fdudi/OneDrive/Desktop/PythonHomework/rosalind_data/advent5_input.txt"
# )

rules = ('''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13''')

updates_examples = '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

update_list = (updates_examples.strip().splitlines())

# print(update_list)

# print(rules.strip().splitlines())

rules_list = (rules.strip().splitlines())

def build_updates():
    updates_new = []
    for numbers in update_list:
        numbers = numbers.split(',')
        row = []
        for number in numbers:
            row.append(int(number))
        updates_new.append(row)
    return updates_new

# print(build_updates())

def build_rules():
    new_list = []
    for pairs in rules_list:
        pairs = (pairs.split('|'))
        x = int(pairs[0])
        y = int(pairs[1])
        new_list.append([x,y])
    return new_list

# print(build_rules())


# find all ys for provided x      
def find_ys(x):
    ys = []
    # go through lists in build rules
    for pairs_rules in build_rules():
        # go through the x and y in pair rules
        if x == pairs_rules[0]:
            ys.append(pairs_rules[1])
    return ys

# print(find_ys(75))

for (idx, update) in enumerate(build_updates()):
    print(f"This is row {idx}")
    for (num, x) in enumerate(update):
        print(f"This is number {x}")
        ys = find_ys(x)
        fulfils_rules = True
        for rest_index in range(num + 1, len(update)):
            if update[rest_index] not in ys:
                fulfils_rules = False
        
            

# Step 1: Compare EVERY LIST in updates to EVERY LIST in rules. Go over each number, whereas first it should be checking the rules lists content.
# Step 2: Rules list content goes over each number in the updates lists.
# Step 3: Create conditions (if the order is ok, keep the list and put it into a new one. if its not, skip it)
# Step 4: Find a way to take the middle number of each valid list and put it into its own list and then add em all together!
# Step 5: gg(?)
