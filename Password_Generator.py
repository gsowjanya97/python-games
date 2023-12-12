#This code is to generate a random password of minimum 8 characters long with at least 1 lower case, 1 upper case, 1 number and 1 special character included. 

import string
import random

def passgen():
    try:
        len = int(input('Please enter the length of the password required (minimum 8 characters): '))
        if len < 8:
            print('Minimum length should be 8 characters! Please try again.')
            return passgen()
    except ValueError:
        print('Please enter a valid number!')
        return passgen()
    
    pwd = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation, k=len-4)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
        
    pwd_shuffled = random.sample(pwd,len)

    print('Here\'s you\'re password: ', ''.join(pwd_shuffled))

print('Welcome to Password Generator!')
passgen()

