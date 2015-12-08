import random
import time
time.clock()
random.randint(4,44)


def SelectCave():
    Cave1 = random.randint(44,77)
    Cave2 = random.randint(78,100)
    print('Select a cave among below 2')
    time.sleep(1)
    print(str(Cave1)+' or '+str(Cave2))
    ChosenCave = input()

    while int(ChosenCave) != int(Cave1) and int(ChosenCave) != int(Cave2):
        print('Wrong Selection! Chose again.')
        print('Select a cave among below 2')
        print(str(Cave1)+' or '+str(Cave2))
        ChosenCave = input()
    return (int(ChosenCave),int(Cave1),int(Cave2))

def DisplayIntro():
    print('Welcome to the Dragon Realm!')
    time.sleep(1)
    print('You can choose one of the available caves presented to you.')
    time.sleep(1)
    print('Select a Cave; you might be handed a treasure or be eaten!')
    time.sleep(1)
    ChosenCave = SelectCave()
    return ChosenCave
PlayAgain = 'Y'
while PlayAgain == 'Y' or PlayAgain == 'y':
    Result = DisplayIntro()
    CaveChoice = Result[0]
    LuckyCave = random.sample(set([int(Result[1]),int(Result[2])]),1)
    if CaveChoice == LuckyCave:
        print('You are walking into the Cave...')
        time.sleep(2)
        print("You are hearing dragon steps...")
        time.sleep(2)
        print('Dragon arrives in front of you..')
        time.sleep(5)
        print('Its your lucky day; you got the treasure!')
        time.sleep(1)
        print('Do you want to try again? Enter \'Yes\' or \'Y\' ')
        PlayAgain = input()
    else:
        print('You are walking into the Cave...')
        time.sleep(2)
        print("You are hearing dragon steps...")
        time.sleep(2)
        print('Dragon arrives in front of you..')
        time.sleep(5)
        print('You are out of luck, Good bye! num num num....')
        time.sleep(1)
        print('Do you want to try again? Enter \'Y\' or \'y\' ')
        PlayAgain = input()
print('Thanks for playing. Good bye!')
exit()
