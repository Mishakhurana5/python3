import random

secret = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess (the number should be between 1 and 50): "))
    if guess == secret:
        print("Congrats! you have guessed the number!")
    elif guess > secret:
        print("You guessed too high!")
    elif guess < secret:
        print("You guessed too low!")
    elif guess >= secret + 20 or guess <= secret - 20:
        print("Ice Cold")
    elif guess >= secret +10 or guess <= secret - 10:
        print("Cold")
    elif guess >= secret +5 or guess <= secret - 5:
        print("Warm")
    else:
        print("Hot")

attempts = attempts - 1
print("Hearts:", end=" ")
for i in range(attempts):
        print("❤️", end="")
    
if attempts == 0:
    print(" \n The game is over you lost! the number was", secret,"Try again?")
