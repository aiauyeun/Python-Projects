# assignment: programming assignment 1
# author: (write your full name here)
# date: (write the date you finished working on the program)
# file: hangman.py is a program that (put the description of the program)
# input: (write input description)
# output: (write output description)

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
        size = int(input("Welcome to the Hangman Game! \n\nPlease choose a size of a word to be guesssed [3-12, default any size]:"))
        if(size > 12 or size < 3):
            raise ValueError
        print("The word size is set to %s." % (size))
    except:
        print("A dictionary word of any size will be chosen")
        size = True
    try:
        lives = int(input("Please choose a number of lives [1-10, default 5]:"))
        if(lives > 10 or lives < 1):
            raise ValueError
        print("You have %s lives" % (lives))
    except:
        print("You have 5 lives")
        lives = 5
    
    return (size, lives)



# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary('dictionary.txt')

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary

    # print a game introduction

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    continq = "Y"
    while(continq.upper() == "Y"):
        # set up game options (the word size and number of lives)
        (size,lives) = get_game_options() 
        # select a word from a dictionary (according to the game options)
        # use choice() function that selects an item from a list randomly, for example:
        # mylist = ['apple', 'banana', 'orange', 'strawberry']
        # word = choice(mylist)
        if size == True:
            rand = randint(3,12)
            hang_word = choice(dictionary[rand])
        else:
            hang_word = choice(dictionary[size])
        hang_word = hang_word.upper()
        print(hang_word)
        let_set = set()
        bar = ""
        lives_vis = ''
        chosen = []
        top = "Letters chosen:"
        xwrong = 0
        win = False
        for letter in hang_word:
            let_set.add(letter.upper())
 
        for i in range(lives):
            lives_vis += '0'
        for i in range(len(hang_word)):
                bar += "_"
        if '-' in hang_word:
            ind = hang_word.find('-')
            bar = bar[:ind] + "-" + bar[ind+1:]
        

        

            # START GAME LOOP   (INNER PROGRAM LOOP)
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        while lives > 0:
            bottom = bar + "   lives: %s   %s" % (lives,lives_vis)
            print(top)
            print(bottom)
            pos_lst = []
            

            # ask the user to guess a letter
            guess = input("Please choose a new letter >")
            if guess.isalpha() == True and len(guess) == 1:
                while guess.upper() in chosen:
                    print("You have already chosen this letter")
                    guess = input("\nPlease choose a new letter >")
                chosen.append(guess.upper())
                top = top + " %s," % (chosen[-1])
            
                if chosen[-1] in let_set:
                    print("You guessed right!")
                    for pos,char in enumerate(hang_word):
                        if(char == chosen[-1]):
                            pos_lst.append(pos)
                    for position in pos_lst:
                        bar = str(bar[:position]) + chosen[-1].upper() + str(bar[position+1:])
                else:
                    print("You guessed wrong!")
                    lives -= 1
                    lives_vis = str(lives_vis[:xwrong] + 'X' + str(lives_vis[xwrong + 1:]))
                    xwrong += 1
            else:
                guess = input("That's not a valid input! Pick Again! >")

            if bar == hang_word:
                win = True
                break
        if win == True:
            print("Congratulations!!! You won! The word is " + hang_word + "!")
        else:
            print("You lost! The word is " + hang_word + "!")
        continq = input("Would you like to play again [Y/N]?")
    print("Goodbye!")
        
    


            

        

            

        

        
        # update the list of chosen letters
        

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program