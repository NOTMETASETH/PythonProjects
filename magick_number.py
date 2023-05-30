# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # this condition is for the correct guess


if guess == secretNumber:
    print('Eureka! You guessed the magick number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Incorrect. The number is magick and your are obviously a muggle ... it was ' + str(secretNumber))
    

print('You took ' + str(guessesTaken) + ' guesses.')
