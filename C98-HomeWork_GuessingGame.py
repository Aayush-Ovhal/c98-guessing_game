import random

number = random.randint(1, 9)


chances = 0

while chances < 5:

    guess = int(input("Guess the number: "))
    
    if guess == number:
        print("Congrats! You won")
        break
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    chances += 1

    if chances == 5:
        print("You Lose!!! you noob!! The number is", number)

    
