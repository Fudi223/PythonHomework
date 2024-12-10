
# the word that is searched for:
victory_word = "SCARF"
while True:
    # input prompt: 
    # print("GUESS THE 5 LETTER WORD! If a letter is the correct one at the correct position, you will get a 'O' sign! If you have the right letter but it is at the wrong position, you will get a '/' sign! If a letter is wrong and at the wrong position, you will get a 'X' sign. Good luck!")
    word_input = input("Which word do you want to try? : ")

    # letter_grid = "O_O_O_O_O"

    # check if a letter from the correct word is present and returns whether the position is correct where its standing, or not.
    wlwp_grid = ""
    # wlwp = Wrong Letter Wrong Place
    # go over every letter in the input word
    for w_letter, v_letter in zip(victory_word, word_input):
        # compare every letter from the input word to the victory word
        if w_letter == v_letter:
            wlwp_grid += "O"
        else:
            if w_letter != v_letter:
                wlwp_grid += "X"
    print(wlwp_grid)
    
    if word_input == victory_word:
        break
