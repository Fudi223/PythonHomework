
# the word that is searched for:
victory_word = "SCARF"

# input prompt: 
print("GUESS THE 5 LETTER WORD! If a letter is the correct one at the correct position, you will get a 'O' sign! If you have the right letter but it is at the wrong position, you will get a '/' sign! If a letter is wrong and at the wrong position, you will get a 'X' sign. Good luck!")
word_input = input("Which word do you want to try? : ")

while word_input != victory_word:
    print("Try again!")
    word_input = input("Which word do you want to try? : ")
    
print("Congratulations!")
# if victory_word == word_input:
#   print("O O O O O")
#   print("Congratulations!")

# if victory_word != word_input:
#   print("X X X X X")
#   print("Try again!")

