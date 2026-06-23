import random
playing = True
number = str(random.randint(0, 9))
print("I will generate a random number between 0 and 9. One digit at a time, Can you guess it?")
print("The game ends when you get 1 hero point!")
while playing:
    guess = input("Give me your best guess! :")
    if number == guess:
        print("You guessed it correctly! You have earned your first hero point!, meaning you won the game!!")
        print("The number was: " , number)
        break
    else:
        print("Your guess was incorrect! You can try again! \n")





import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break



import math

print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))

x = 10
y = -15
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))