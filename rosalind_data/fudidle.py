

victory_word = "SCARF"
# I didnt implement this yet properly but I want to make sure that if a word is entered that is longer than 5 letters, it should say "Word has to be 5 letters long" and return to the input.
number5 = len(victory_word)
# Game Rules
print(f'''GUESS THE {number5} LETTER WORD! If a letter is the correct one at the correct position, you will get a 'O' sign! 
If you have the right letter but it is at the wrong position, you will get a '/' sign! 
If a letter is wrong and at the wrong position, you will get a 'X' sign. Good luck!''')

while True:
    # input prompt: 
    word_input = input("What is the word? : ")

    # letter_grid = "O_O_O_O_O"

    # check if a letter from the correct word is present and returns whether the position is correct where its standing, or not.
    correct_or_wrong_grid = ""
    # go over every letter in the input word and victory word
    for letterA, letterB in zip(victory_word, word_input):
        # compare each letter, if its the same, print "O" into the grid
        if letterA == letterB:
            # add "O" to the grid if correct
            correct_or_wrong_grid += "O"
        else:
            if letterB in victory_word:
                correct_or_wrong_grid += "/"
        # add "X" to the grid if the letter is wrong
            else:
                if letterA != letterB:
                    correct_or_wrong_grid += "X" 
    print(correct_or_wrong_grid)

    # exit the loop if the right word is entered
    if word_input == victory_word:
        break
print("Congratulations, you found the word!")