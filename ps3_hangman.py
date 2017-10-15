# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
chosenWord=chooseWord(wordlist)
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is "  + str(len(chosenWord)) + " letters long.")
guess_counter=8
found=False
print("secilen",chosenWord)
model=("_ "*len(chosenWord)).split()
predicted_letters=[]
while  guess_counter > 0 or found:
    
    
    letters="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    print("You have "+str(guess_counter)+" left")
    letter=input()
    print(predicted_letters)
    if letter in predicted_letters:
        print("Oops! You've already guessed that letter: "+" ".join(model))
    elif letter in chosenWord:
        
        for i in range(len(chosenWord)):
            if letter == chosenWord[i]:
                
                model[i]=letter
        predicted_letters.append(letter)
        print("Good guess: "+" ".join(model)) 
    
        
    else:
        print("Oops! That letter is not in my word: "+" ".join(model))
        guess_counter-=1
   
    if "".join(model) == chosenWord:
        print("Congratulations, you won!")
        found=True
        break
    
    del(letters[ord(letter[:1])-97])

    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
    
if guess_counter==0:
    print("Sorry, you ran out of guesses. The word was else. ")






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
