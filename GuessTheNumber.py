import random
TurnCount = 0

def GetRand():
    RandNum = random.randint(1,20)
    return RandNum

def NumCheck(PlayerNum,RandNum):
    if PlayerNum == RandNum:
        return 's'
    elif PlayerNum < RandNum:
        return 'l'
    else:
        return 'h'

print("Hello What is your Name? ")
PlayerName = input()
print("Its nice to meet you "+ PlayerName)
print("Lets play a game! Guess a number between 1 and 20")
while TurnCount < 6:
    PlayerNum = input()
    PlayerNum = int(PlayerNum)
    RandNum = GetRand()
    Result = NumCheck(PlayerNum,RandNum)
    if Result == 's':
        print('Your Guess is Right! Good bye.')
        exit()
    elif Result == 'l':
        print('Number too low! Guess Again ')
    elif Result == 'h':
        print('Number too high! Guess Again ')
    else:
        print('No Output')
        exit()
    TurnCount = TurnCount + 1
print('\nYou are out of guesses! Good Bye.')