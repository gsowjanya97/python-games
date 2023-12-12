import random

n = random.randrange(0, 100, 10)

#Maximum 5 chances are given to guess
c = 5

print('Welcome to the Number Guessing Game!')

def guess():

    global c #Defining global variable
    
    try:
        var = int(input('Guess a number between 1 to 100: '))
    except ValueError:
        print('This is not a valid number... Please try again)')
        return guess()

    if var > n:
        print('Too High! Guess a number lower than this')
        c -= 1
        if c == 0:
            print('You\'ve exceeded 5 attempts! Sorry :(')
            return
        else:
            return guess()
    
    elif var < n:
        print('Too Low! Guess a number higher than this')
        c -= 1
        if c == 0:
            print('You\'ve exceeded 5 attempts! Sorry :(')
            return
        else:
            return guess()
    
    else:
        print('You guessed it right! Congratulations :D')

guess()
