import random
import time
import os
SecretWord = 'Dice'
def CreateNewHangman(SecretWord,GuessWord):
    if GuessWord == 0:
        for i in range(0,len(SecretWord)):
            print('_ ',end='')
        print()
        print()
        print('-XXX-')
        print('|    |')
        print('     |')
        print('     |')
        print('     |')
        print('_____|')
    else:
        for i in range(0,len(SecretWord)):
            if (SecretWord[i].upper() in GuessWord) or (SecretWord[i].lower() in GuessWord):
                print(SecretWord[i],end='')
            else:
                print('_',end='')

        print()
        print()
        print('-XXX-')
        print('|    |')
        print('     |')
        print('     |')
        print('     |')
        print('_____|')

PlayChoice = 'Y'
GoodKarma = 0
BadKarma = 0
GuessWord = ''
CreateNewHangman(SecretWord,0)
while PlayChoice == 'Y' or PlayChoice == 'y':
    print('Guess a letter')
    GuessLetter = input()
    while (GuessLetter in GuessWord):
        print('Letter guessed prior. Try again!')
        GuessLetter = input()
    GuessWord = GuessWord + GuessLetter
    if (GuessLetter.upper() in SecretWord) or (GuessLetter.lower() in SecretWord):
        GoodKarma = GoodKarma + 1
        CreateNewHangman(SecretWord,GuessWord)
    elif not((GuessLetter.upper() in SecretWord) or (GuessLetter.lower() in SecretWord)):
        BadKarma = BadKarma + 1
        print('Number of Guesses left: ',len(SecretWord)-int(BadKarma))
    else:
        print()

    if GoodKarma == len(SecretWord):
        print('You Win!')
        exit()
    if BadKarma == len(SecretWord):
        print('You Lose!')
        exit()



