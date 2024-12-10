
# from util import read_input:
from util import read_input
from random_1 import randint
# import the list of words
random_words = read_input("C:/PythonHomework/rosalind_data/Valid-Wordle-Words.txt")
# use the RNG to get an integer that ranges from pos. 0 all the way to the last position in the list of words
picked_line = randint( 0, len(random_words))
# use random picked integer to take the word on the corresponding line and print it

victory_word = "".upper()
for i, line in enumerate(random_words):
    picked_word = ""
    if i == picked_line:
        picked_word += line
        victory_word += picked_word

# print(victory_word)
# I didnt implement this yet properly but I want to make sure that if a word is entered that is longer than 5 letters, it should say "Word has to be 5 letters long" and return to the input.

# Game Rules
print('''GUESS THE 5 LETTER WORD! If a letter is the correct one at the correct position, you will get a 'O' sign! 
If you have the right letter but it is at the wrong position, you will get a '/' sign! 
If a letter is wrong and at the wrong position, you will get a 'X' sign. Good luck!''')

while True:
    # input prompt: 
    word_input = input("What is the word? : ")

    # letter_grid = "O_O_O_O_O"

    # check if a letter from the correct word is present and returns whether the position is correct where its standing, or not.
    correct_or_wrong_grid = ""
    # go over every letter in the input word and victory word
    for letterA, letterB in zip(victory_word.casefold(), word_input.casefold()):
        # compare each letter, if its the same, print "O" into the grid
        if letterA == letterB:
            # add "O" to the grid if correct
            correct_or_wrong_grid += "O"
        
        else:
            if letterB in victory_word.casefold():
                correct_or_wrong_grid += "/"
        # add "X" to the grid if the letter is wrong
            else:
                if letterA != letterB:
                    correct_or_wrong_grid += "X" 
    print(word_input.upper())
    print(correct_or_wrong_grid.upper())

    # exit the loop if the right word is entered
    if word_input.casefold() == victory_word.casefold():
        break
print("Congratulations, you found the word, " + victory_word.upper() + "!")
