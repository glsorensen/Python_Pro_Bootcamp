import random

def guessing_game():

    def difficulty():
        print("Hello, Welcome to the guessing game!")
        print("The computer will pick a number between 1 and 100\nand your goal is to pick that number in the defined number of guesses.")

        while True:  # Start an infinite loop
            response = input("Would you like to play on easy (10 guesses) or hard (5 guesses)\n").strip().lower()

            if response == "easy":
                print("You have picked easy and will have 10 guesses.")
                return response
            elif response == "hard":
                print("You have picked hard and will have 5 guesses.")
                return response
            else:
                print("Incorrect entry, please enter 'easy' or 'hard'.")

    user_choice = difficulty()

    def max_attempts():
        if user_choice == "easy":
            user_attempts = 10
            return user_attempts
        else:
            user_attempts = 5
            return user_attempts
    user_attempts = max_attempts()
    random_number = random.randint(0, 101)
    attempt_count = 0

    while attempt_count < user_attempts:

        try:
            guess = int(input("Please enter a number between 0 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess == random_number:
            print("Congratulations, you win!" )
            print(f"The number was {random_number}")
            break
        elif guess > random_number:
            print("The number is lower.")
        else:
            print("The number is higher.")
        attempt_count += 1
    if attempt_count == user_attempts:
        print(f"Sorry, you've used all your attempts. The number was {random_number}.")


def main():
    while True:
        guessing_game()
        retry = input("Do you want to play again? (yes/no): ").strip().lower()

        if retry != 'yes':
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()