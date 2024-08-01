# https://cs50.harvard.edu/python/2022/psets/4/game/
import random

n = 0 # Level form user
num = 0 # Random num form 1 to level
guess = 0 # Guess form the user

# User input [if not +ve ==> prompt again]
while True:
    try:
        while True:
            n = int(input("Level: "))
            if n >= 1:
                break
            else:
                continue
        break
    except:
        continue

# random int from 1 to level
num = random.randint(1, n)

# prompt to guss number [if not +ve ==> prompt again]
while True:
    try:
        while True:
            guess = int(input("Guess: "))
            if guess >= 1:
                # Final conditions
                if guess < num:
                    print("Too Small!")
                elif guess > num:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            else:
                continue
        break
    except:
        continue
