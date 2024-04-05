import random

top_of_range = input("Type a number: ")


top_of_range = int(top_of_range)
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    userGuess = input("Make a guess: ")
    userGuess = int(userGuess)
    if random_number == userGuess:
        print("You got it!")
        break
    elif random_number > userGuess:
        print("You are below the number!")
    else:
        print("You are above the number!")

    guesses += 1

print("You got it ", guesses)

