from util import read_input
from random_1 import randint
# import the list of words
random_words = read_input("C:/PythonHomework/rosalind_data/Valid-Wordle-Words.txt")
# use the RNG to get an integer that ranges from pos. 0 all the way to the last position in the list of words
picked_line = randint( 0, len(random_words))
# use random picked integer to take the word on the corresponding line and print it

for i, line in enumerate(random_words):
    picked_word = ""
    if i == picked_line:
        picked_word += line
        print(picked_word)



