import random

class GuessingGame:
    def __init__(self, min_num, max_num, max_attempts):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"Enter your guess between {self.min_num} and {self.max_num}: "))
                if self.min_num <= guess <= self.max_num:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def play(self):
        print(f"Welcome to the Guessing Game! You have {self.max_attempts} attempts.")
        while self.attempts < self.max_attempts:
            guess = self.get_user_guess()
            self.attempts += 1
            if guess < self.secret_number:
                print("Too low! Try guessing a higher number.")
            elif guess > self.secret_number:
                print("Too high! Try guessing a lower number.")
            else:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                return
        print(f"Sorry, you've used up all your attempts. The correct number was {self.secret_number}.")



min_num = 1
max_num = 100
max_attempts = 10

game = GuessingGame(min_num, max_num, max_attempts)
game.play()
