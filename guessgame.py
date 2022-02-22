# guessgame.py
# the system will choose a random number between any ranges defined
# the user is given a hint to guess the number
# every time the user guesses the number incorrectly he is given another hint to guess the answer
# clue can be any type like <, >, *, / etc.
# include a function to check if the input is correct or not

import random
import operator

# fixed number of guesses
GUESSES = 3

def welcome_message():
    print("Welcome to my CLI game, 'Guess the Number'! You will \
guess a number, and I will give you a hint if it is correct or not. Here, let me give you a first hint!:\n")
welcome_message()


# generate random number
def generate_the_number ():
    the_number = random.randint(1,9)
    return the_number

# generate the number
# generate the hint for the number
# get and verify input
# if number is wrong; give another hint

# generate the hint for the user based on the random number generated
def hint_for_user():
    answer = generate_the_number()
    if answer % 2 == 0:
        print ("The number is even!\n")
    else:
        print ("The number is odd!\n")
    return answer

# verify the user's input is a legitimate guess
def guess_the_number():
    the_answer = hint_for_user()
    for guess in range(GUESSES):
        guess_from_user = int(input("Please type your guess for what the number is!\n"))
        if guess_from_user < the_answer:
            print("Your guess is too low! Please guess again!\n")
        elif guess_from_user == the_answer:
            print("Correct! This is the correct number!\n")
        elif guess_from_user > the_answer:
            print("Your guess is too high! Please guess again!\n")
    
    print("The game is over. Thank you for playing my CLI game! ^.^")
guess_the_number()







