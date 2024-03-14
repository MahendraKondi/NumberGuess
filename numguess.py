import random
print("Welcome to number guessing game")
number = int(input("Type a number: "))
random_num = random.randint(1,number)
guess = 0
while True:
    guess += 1
    num_guess = int(input("Make a guess: "))
    if num_guess == random_num:
        break
    elif num_guess > random_num:
        print("You have guessed above!")
    else:
        print("You have guessed below!")

print("You have guessed correct number in",guess,"guesses:)")