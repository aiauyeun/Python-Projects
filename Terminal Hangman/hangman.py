# assignment: Hangman
# author: Aidan Au-Yeung
# date: 10/6/22
# file: hangman.py is a program that lets you play the popular game 'hangman'
# input: text file, letters, number of lives, size of the word, option to play again
# output: instructions for the game, words guessed, correct words guessed, amount of lives, option a choose a new letters, solution to game after finishing, welcome statement, win statement and goodbye statement

from curses.ascii import isalpha
from random import choice, random, randint

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    with open(filename,'r') as file:
        for line in file.readlines():
            for word in line.strip().split(" "):
                if len(word) > 0:
                    if len(word) <= max_size:
                        try:
                                dictionary[len(word)].append(str(word))
                        except:
                            dictionary[len(word)] = [word]
                    else:
                        dictionary[12].append(word)
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("\nPlease choose a size of a word to be guessed [3 - 12, default any size]:"))
        if(size > 12 or size < 3):
            raise ValueError
        print("\nThe word size is set to %s." % (size))
    except:
        print("A dictionary word of any size will be chosen")
        size = True
    try:
        lives = int(input("Please choose a number of lives [1-10, default 5]:"))
        if(lives > 10 or lives < 1):
            raise ValueError
        print("\nYou have %s lives." % (lives))
    except:
        print("\nYou have 5 lives.")
        lives = 5
    
    return (size, lives)

#picks the a word from the imported txt file depending on the input size. If no size is entered, a word of a random length will be picked
def pick_word (size):
    if size == True:
        rand = randint(3,12)
        word = choice(dictionary[rand])
    else:
        word = choice(dictionary[size])
    return word.upper()

#generates a nonrepeating set of letters that are used to spell the target word
def letters (word):
    let_set = set()
    for letter in hang_word:
        let_set.add(letter.upper())
    return let_set
        

#generates a bar that is equal to the length of the word. If the target word has "-" in it, it will automatically be filled in
def gen_bar (word):
    bar = []
    for letter in word:
        bar.append("__ ")
    if '-' in word:
        bar[word.rfind("-")] = "-"
        
    return bar

    

#makes the visual for lives in the game. exp 8 lives = 00000000 
def format_lives (lives):
    lives_vis = ''
    for i in range(lives):
        lives_vis += 'O'
    return lives_vis

    






# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary('dictionary.txt')

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary

    # print a game introduction

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    continq = "Y"
    print("Welcome to the Hangman Game!")
    while(continq.upper() == "Y"):
        # set up game options (the word size and number of lives)
        (size,lives) = get_game_options() 
        # select a word from a dictionary (according to the game options)
        # use choice() function that selects an item from a list randomly, for example:
        # mylist = ['apple', 'banana', 'orange', 'strawberry']
        # word = choice(mylist)
        hang_word = pick_word(size)
        bar = gen_bar(hang_word)
        let_set = letters(hang_word)
        lives_vis = format_lives(lives)
        chosen = []
        top = "Letters chosen:"
        xwrong = 0
        win = False
        win_set = set()
        if '-' in hang_word:
            win_set.add("-")

        

        

        

            # START GAME LOOP   (INNER PROGRAM LOOP)
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        while lives > 0:
            bottom = ' '.join(bar) + "lives: %s %s" % (lives,lives_vis)
            pos_lst = []
            guess_valid = False
            print(top)
            print(bottom)
            if win_set == let_set:
                win = True
                break

#checks if the guess is valid
            guess = input("Please choose a new letter >")
            while guess_valid == False:  
                if guess.upper() in chosen:
                        print("\nYou have already chosen this letter.")
                        guess = input("\nPlease choose a new letter >")
                        guess_valid = False
                elif guess.isalpha() and len(guess) == 1:
                    guess_valid = True
                    chosen.append(guess.upper())
                else:
                        guess = input("\nPlease choose a new letter >")
                        guess_valid = False
#checks if the guess is right and modifies the output to match the input
            if len(chosen) <= 1:
                top = top + " %s" % (chosen[-1])
            else:
                top = top +", %s" % (chosen[-1])
            
            if chosen[-1] in let_set:
                print("\nYou guessed right!")
                win_set.add(chosen[-1])
                for pos,char in enumerate(hang_word):
                    if(char == chosen[-1]):
                        pos_lst.append(pos)
                for position in pos_lst:
                    bar[position] = chosen[-1] + " "
            else:
                print("\nYou guessed wrong, you lost one life.")
                lives -= 1
                lives_vis = str(lives_vis[:xwrong] + 'X' + str(lives_vis[xwrong + 1:]))
                xwrong += 1

                    

#End of game loop. Decides what happens if win is true or false         
        if win == True:
            print("Congratulations!!! You won! The word is " + hang_word + "!")
        else:
            xwrong -= 1
            bottom = ' '.join(bar) + "lives: %s %s" % (lives,lives_vis)
            print(top)
            print(bottom)
            print("You lost! The word is " + hang_word + "!")
        #Gives option to continue playing!
        continq = input("Would you like to play again [Y/N]?")
    print("\nGoodbye!")
