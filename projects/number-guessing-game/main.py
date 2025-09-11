import random

print("Hey! Welcome to the Number Guessing Game. \nYou have maximum 7 chances to find the number.\n")

low = int(input("Enter the low bound: "))
high = int(input("Enter the high bound: "))

number = random.randrange(low, high)

print(f"\nYou have 7 chnaces to find the number between {low} and {high}. Let's start.")

chances = 6
count = 0

while count <= chances:
    count += 1

    guess = int(input("\nEnter your guess: "))

    if guess == number:
        print(f"Correct! The number is {number}. You guessed it in {count} attepts.")
        break
    elif count > 6:
        print(f"Incorrect! You tried too many time. The number was {number}. You will get better next time.")
        break
    elif guess > number:
        print("Too high. Try a lower number.")
    elif guess < number:
        print("Too low. Try a higher number.")
