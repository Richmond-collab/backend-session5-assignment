import random

secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print(f"Correct! You won in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. You lost!")
    print(f"The secret number was {secret_number}.")