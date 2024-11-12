#LINES 68-75 COMPRISE MY ADDITION TO THE CODE, I HAVE ADDED A CHEAT CODE WHICH ENABLES THE USER TO BYPASS THE WHOLE THING.



print('Hello. Welcome to the maze. To escape the maze, you must either defeat one of the monsters, or find your way out. Good luck. ')

decision = input('You are now inside the maze. There is no turning back. Would you like to go LEFT, RIGHT, or FORWARD? ')
if decision.upper() == 'LEFT':
    decision = input('An enormous spider blocks your path! Will you RUN or FIGHT? ')
    if decision.upper() == 'FIGHT':
        decision = input('Will you use your TASER or your BATON? ')
        if decision.upper() == 'BATON':
            print('You beat the spider! Congrajulations! ')
        elif decision.upper() == 'TASER':
            print('That did not work and you died. Game over.')
        else:
            print('Your selection is not valid, and you must restart the game. ')
    elif decision.upper() == 'RUN':
        decision = input('Running will result in leaving the game. Would you like to PLAY or QUIT? ')
        if decision.upper() == 'PLAY':
            decision = input('Wise choice friend. Will you use your CANON or your FIST to fight the spider? ')
            if decision.upper() == 'CANON':
                print('You could not load the canon in time, and died. You lose.')
            elif decision.upper() == 'FIST':
                print('You have beaten the spider. You win!')
            else:
                print('Your selection is not valid, and you must restart the game. ')
        elif decision.upper() == 'QUIT':
            print('You have quit the game...chicken. ')
        else:
            print('Your selection is not valid, and you must restart the game. ')
    else:
        print('Your selection is not valid, and you must restart the game. ')
elif decision.upper() == 'RIGHT':
    decision = input('You have gone right, and have found yourself with another decision to make. Will you go LEFT or RIGHT? ')
    if decision.upper() == 'LEFT':
        decision = input('Yet another crossroads. Will you go STRAIGHT or RIGHT? ')
        if decision.upper() == 'STRAIGHT':
            print('You have died on starvation...loser. ')
        elif decision.upper() == 'RIGHT':
            print('You have escaped the maze. Congrajulations! ')
        else:
            print('Your selection is not valid, and you must restart the game. ')
    elif decision.upper() == 'RIGHT':
        decision = input('You have reached yet another crossroads. Will you go RIGHT or LEFT? ')
        if decision.upper() == 'RIGHT':
            print('You have escaped the maze. Good job. ')
        elif decision.upper() == 'LEFT':
            print('You have died of terminal dehydration...loser. ')
        else:
            print('Your decision is not valid. Please restart the game. ')
    else:
        print('This is not a valid option. Please restart the game. ')
elif decision.upper() == 'FORWARD':
    decision = input('You have gone forward in the maze and have found yourself in a crossroads. Would you like to go RIGHT or LEFT? ')
    if decision.upper() == 'RIGHT':
        decision = input('Yet another crossroads, would you like to go FORWARD or RIGHT? ')
        if decision.upper() == 'FORWARD':
            print('You have escaped the maze. Victory! ')
        elif decision.upper() == 'RIGHT':
            print('You have died due to a lack of love...lonely loser. ')
        else:
            print('Your selection is not a valid one. Please restart the game. ')
    elif decision.upper() == 'LEFT':
        decision = input('Oh no! A giant snake is chasing you! Will you PANIC or FIGHT? ')
        if decision.upper() == 'PANIC':
            print('You have paniced and died. Scaredy cat... ')
        elif decision.upper() == 'FIGHT':
            print('You beat the snake, and unlocked the cheat code. The code must be entered at the first question of the game: DREWSTANLEYISTHEBEST. ')
        else:
            print('This is not a valid option. Please restart the game. ')
elif decision.upper() == 'DREWSTANLEYISTHEBEST':
    decision = input('You have activated the cheat code eater egg. You may now go to the end of the maze. Would you like to do this? Anwer with YES or NO. ')
    if decision.upper() == 'YES':
        print('Congrajulations. You win even though you cheated. ')
    elif decision.upper() == 'NO':
        print('Very well. Please restart the game. ')
    else:
        print('This is not a valid option. Please restart the game. ')
else:
    print('This is not a valid option. Please restart the game. ')
