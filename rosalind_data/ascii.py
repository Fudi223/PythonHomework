# This is the attempt at making a ASCII art drawing script

# Goal: Draw a pyramid with as many lines as the user puts into the prompt.

# First idea: Make a loop that keeps adding "/" and "\" characters for as many lines as are input.

# What needs to be taken in account?
# -The tip of the pyramid must not be right at the beginning of the line. It needs to start as far in the middle as is required based on the input number
# -in the last line, the "/" has to be at the first position of the line.
# -The final line should be the baseline of the pyramid, made with "_" (So if input=10, 9 lines will be sides and the 10th will be the base)

# This will require a loop and a input prompt. The prompt should look like this:

# Ask the user to write how tall the pyramid should be

pyramid_size = int(input("How tall is the Pyramid? "))

# Then there should be the loop to print the specified number of lines that was put in, but I want to try to also have the ammount of spaces equal to the number for now.

# for i in range(pyramid_size):
#     print(" ", end="")
# print()

# A dictionary might work out here, I dont think it needs to be as complicated as my first itteration.
# I checked online and found out I can use "end=""" to have the values printed next to each other without a space inbetween
# The dictionary seems to work!

pyramid_sides_dictionary = {"left_side": "/", "right_side": "\\"}

# for sides in pyramid_sides_dictionary.values():
#     print(sides, end="")

# The next step then would be creating a loop and have the input prompt implemented (I think).

# for left in pyramid_sides_dictionary["left_side"]:
#     if left != left[0:]:
#             print(left)
#     else:
#         if left == left[0:]:
#              print(left, pyramid_size)
#     print()


# After consulting the internet, it seems like this solution is overly complicated.
# Here is what I found that should probably work:

# for i in range(pyramid_size): 
#     for j in range(pyramid_size - i - 1):
       
#         print(" ", end="")
   
#     print(pyramid_sides_dictionary["left_side"], end="")
    
#     if i > 0:
#         for k in range(2 * i - 1):
       
#             print(" ", end="")

#     print(pyramid_sides_dictionary["right_side"], end="")
    
#     print()


# the second row doesnt work, I dont know what to do





