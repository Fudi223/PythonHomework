# This will be my new attempt at making a script that draws ASCII art, this time a square.

# As with the triangle, lets have an input prompt:
square_dimensions = int(input("What are the squares dimensions: "))

# So if we have the input=6, a 6x6 square should be printed, using a lowercase "o"

# o o o o o o
# o         o
# o         o 
# o         o   
# o         o
# o o o o o o

# A dictionary might be overkill here? So I will just define the building block ("o") as a variable.

square_element_horiz = "-"
square_element_vert = "|"

# From the triangle, I remember that using a range will be helpful in order to have a variable that can be used for the sides
# To get a filled out square with the correct dimensions, the loops is quite simple:
# for row in range(square_dimensions):
#    print((square_element + " ") * (square_dimensions))
# This works. BUT, I only want to print the sides!

# Here is how to get there without filling the square! 

# Loop takes the number from the input as a range
for row in range(square_dimensions):
    # If left without this if statement, we would end up with one excessive row that would mess up the symmetry
    # Its a bit messy, but if I use square_dimensions - 2, I can just skip that one and still specify an action for
    # the last row later in the loop
    if row == square_dimensions - 2:
        continue
    # this if statement will draw the top side of the square with spaces inbetween to keep symmetry
    if row == 0:
        print((square_element_horiz + " ") * (square_dimensions))
    # this if statement will draw the bottom line of the square, also with spaces
    if row == square_dimensions - 1:
        print((square_element_horiz + " ") * (square_dimensions))
    # And this will be our sides, with the first position in the row being the "o", then spaces inbetween that are
    # calculated by the input number times two and minus 3.
    else:
        print(square_element_vert +  ((" ") * (square_dimensions * 2 - 3)) + (square_element_vert))

# and thats it! Even is this was way simpler and less complex than the triangle, I still managed to do it without
# ChatGPT. I only had to look up in a "Stackoverflow.com" forum how to skip a row in a loop. Thats how I found
# out I can use "continue".
# Its probably also possible to create the Square using lines by adding a square element and replacing the original one
# Yup, I just tried and even tho it looks a tiny bit awkward at the corners, it technically works! If I can 
# find a symbol or character that would fit the corners, I can probably also add that into the for loop. But for
# now, Im going to bed, its 2am and I am running on 5 hours of sleep. This was very satisfying though!
# -Fudi

  
