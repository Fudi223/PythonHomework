#!/usr/bin/env

# Day 4 Advent



searched_word1 = "XMAS"
searched_word2 = "SAMX"

xmas_crossword = ([
                ["M","M","M","S","X","X","M","A","S","M"],
                ["A","M","X","S","X","M","A","A","M","M"],
                ["M","S","A","M","A","S","M","S","M","X"],
                ["X","M","A","S","A","M","X","A","M","M"],
                ["X","X","A","M","M","X","X","A","M","A"],
                ["S","M","S","M","S","A","S","X","S","S"],
                ["S","A","X","A","M","A","S","A","A","A"],
                ["M","A","M","M","M","X","M","M","M","M"],
                ["M","X","M","X","A","X","M","A","S","X"]])


def horizontal_xmas():
    counter1 = 0
    for line in xmas_crossword:
        line_string = "".join(line)
        count = line_string.count(searched_word1)
        if count > 0:
            counter1 += count
            # print(f"Found {searched_word1} in line: {line} (count: {count})")
            # print(counter1)
    return counter1

def horizontal_xmas_backwards():
    counter2 = 0
    for line in xmas_crossword:
        line_string = "".join(line[::-1])
        count = line_string.count(searched_word2)
        if count > 0:
            counter2 += count
            # print(f"Found {searched_word2} in line: {line} (count: {count})")
            # print(counter2)
    return counter2 

# First number in matrix print = vertical, second horizontal

def vertical_xmas_down():
    counter3 = 0
    nume_columns = len(xmas_crossword[0])
    for col in range(nume_columns):
        vertical_string_top = "".join(row[col] for row in xmas_crossword)
        count = vertical_string_top.count(searched_word1)
        if count > 0:
            counter3 += count
            # print(f"Found {searched_word1} in column: {col} (count: {count})")
            # print(counter3)
    
    return counter3

def vertical_xmas_up():
    counter4 = 0
    nume_columns = len(xmas_crossword[0])
    for col in range(nume_columns):
        vertical_string_top = "".join(row[col] for row in xmas_crossword)
        count = vertical_string_top.count(searched_word2)
        if count > 0:
            counter4 += count
            # print(f"Found {searched_word2} in column: {col} (count: {count})")
            # print(counter4)
    
    return counter4




counter1 = horizontal_xmas()
counter2 = horizontal_xmas_backwards()
counter3 = vertical_xmas_down()
counter4 = vertical_xmas_up()
total_count = counter1 + counter2 + counter3 + counter4
print(total_count)