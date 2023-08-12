import random
while True:
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Try to guess the number between 1 and 100. You only have 10 tries :D")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations, {name}! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
    
    if guess != secret_number:
        print(f"Sorry, {name}. You've used all 10 attempts. The secret number was {secret_number}.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        continue
    else:
        print("Thank you for playing!")
        break
