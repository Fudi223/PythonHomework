#!/usr/bin/env python3

# This is the attempt at making a ASCII art drawing script

# Goal: Draw a pyramid with as many lines as the user puts into the prompt.

# First idea: Make a loop that keeps adding "/" and "\" characters for as many lines as are input.

# What needs to be taken in account?
# -The tip of the pyramid must not be right at the beginning of the line. It needs to start as far in the middle as is required based on the input number or rows
# -in the last line, the "/" has to be at the first position of the line.
# -The final line should be the baseline of the pyramid, made with "_" (So if input=10, 9 lines will be sides and the 10th will be the base)

# This will require a loop and a input prompt. The prompt should look like this:

# Ask the user to write how tall the pyramid should be

pyramid_size = int(input("How tall is the Pyramid? "))

# A dictionary might work out here.
# The dictionary seems to work!

pyramid_sides_dictionary = {"left_side": "/", "right_side": "\\"}

left = pyramid_sides_dictionary["left_side"]
right = pyramid_sides_dictionary["right_side"]        

# The range will take the input number and run it over "row"
for row in range(pyramid_size):
    # spaces_leftside will print from the second last row
    spaces_leftside = pyramid_size - row - 1
    # since the range goes from 0-10, its 11 in total. so for row 1 its spaces_leftside = 11-1-1=9, 11-2-1=8 and so on
    
    # next, there need to be spaces between the "/" and "\", but only from row 2 onwards. in row 1 it should look like this : /\. This will be used in the final print formula
    if row == 0:
        spaces_betweenLR = 0
    
    # however, if we are on the 2nd row, the value from the range is 1 and the formula gives: spaces_betweenLR = 2 * 1=2, 2 * 2 = 4, 2 * 3= 6 etc. 
    else: 
        spaces_betweenLR = 2 * row
    
    # Since the pyramid also needs its base, another if statement is needed to set a condition for the last row. If we are on the last row, the print should add "_" instead of spaces
    # between the "/" and "\"
    if row == pyramid_size - 1: # The last row
        print(" " * spaces_leftside + left + "_" * spaces_betweenLR + right)
    # if we are not at the final line, there should just be spaces!
    else:
        print(" " * spaces_leftside + left + " " * spaces_betweenLR + right)

# Big disclaimer: It took a lot of help from online resources, one after-class hint talk with Niko, and regretfully ChatGPT too. 
# However, I used ChatGPT to check my code and what was wrong with my train of thought without giving me the right code immediately
# Once again, I had the right idea but putting it into "code-words" proved difficult. I kept trying to use slices to check which row I am at etc.
# I hope to be able to make a script to draw another shape based on what I learned here completely on my own. 

