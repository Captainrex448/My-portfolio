import random

print("i'm gonna think of a number between 0 and 100. You have to guess the number")
chosen_number = random.randint(0,100)
user_guess = int(input("go ahead make a guess"))
while user_guess != chosen_number:
    if user_guess < chosen_number:
        user_guess = int(input("Guess higher"))
    else:
        user_guess = int(input("guess lower"))

print("You have guessed the right number")
