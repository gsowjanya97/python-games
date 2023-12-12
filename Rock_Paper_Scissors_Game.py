import random

print("Welcome to Rock Paper Scissors Game!")

u,c = 0,0

def rps():

    global u, c

    arr = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}
    comp = random.choice(list(arr.keys()))
    comp_val = arr.get(comp)

    try:
        user = int(input('''Choose any number of your choice:
                         1 - Rock
                         2 - Paper
                         3 - Scissors
                         4 - Stop the Game

                         '''))
    except ValueError:
        print('Please enter a valid number between 1 and 3')
        return rps()
    
    if user not in range(1,5):
        print('Please enter a valid number between 1 and 3')
        return rps()
    
    elif user == 4:
        if [u,c]!=[0,0]:
            print('You\'re Final Score = ', u, '\nComputer\'s Final Score = ', c)
            if u == c:
                print('It\'s a Tie!')
            elif u > c:
                print('Congratulations! You Won!!!')
            else:
                print('Sorry.. You Lose :(')
        return
    elif user == comp:
        print('You\'re choice: ', arr.get(user), '\nComputer\'s choice: ', comp_val,'\nIt\'s a Tie!')
        return rps()
    elif ((user+1)-comp) in [0,3]:
        print('You\'re choice: ', arr.get(user), '\nComputer\'s choice: ', comp_val, '\nYou Lose!')
        c += 1
        return rps()    
    else:
        print('You\'re choice: ', arr.get(user), '\nComputer\'s choice: ', comp_val, '\nYou Win!')
        u +=1
        return rps()
rps()


