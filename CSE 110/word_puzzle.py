#For my exceeding of expectations, I have added a second  optional stage to the game using the same block of code, but a different word. I have also made sure that the program know how to deal with all reponses.


secret = 'casual'
print('Welcome to the word game. ')
count = 0
hint = '_' *len(secret)
guess = ''
print(f'Hint: {hint}')
while guess != secret:
    guess = input('Make a guess. ').lower()
    count +=1
    if guess == secret:
        print('That is the word. You win! ')
        print(f'Your number of guesses is: {count}')
    elif len(secret) != len(guess):
        print('Guess is incorrect number of letters. ')
    else:
        print(f'Hint: {hint} ')
        for index, letter in enumerate(guess):
            if guess[index] == secret[index]:
                print(letter.upper(), end='')
            elif letter in secret:
                print(letter.lower(), end='')
            else:
                print('_', end='')


answer = input('Would you like to play again? ').upper()
if answer == 'NO':
    print('Thank you for playing! ')
elif answer == 'YES':
    secret = 'ridiculous'
    print('Welcome to the word game stage 2. ')
    count = 0
    hint = '_' *len(secret)
    guess = ''
    print(f'Hint: {hint}')
    while guess != secret:
        guess = input('Make a guess. ').lower()
        count +=1
        if guess == secret:
            print('That is the word. You win! End of game. ')
            print(f'Your number of guesses is: {count}')
        elif len(secret) != len(guess):
            print('Guess is incorrect number of letters. ')
        else:
            print(f'Hint: {hint} ')
            for index, letter in enumerate(guess):
                if guess[index] == secret[index]:
                    print(letter.upper(), end='')
                elif letter in secret:
                    print(letter.lower(), end='')
                else:
                    print('_', end='')
else:
    print('Invalid response. Please exit. ')