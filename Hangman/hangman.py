import random

class Hangman:
    def __init__(self, words, max_attempts=6):
        self.words = words
        self.secret_word = random.choice(words).lower()
        self.guessed_letters = set()
        self.attempts_left = max_attempts

    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.secret_word)

    def guess(self, guess):
        guess = guess.lower()
        if len(guess) == 1:  # Single letter guess
            if guess in self.guessed_letters:
                print("You've already guessed that letter!")
                return
            self.guessed_letters.add(guess)
            if guess not in self.secret_word:
                self.attempts_left -= 1
                print("Incorrect guess. Attempts left:", self.attempts_left)
                if self.attempts_left == 0:
                    print("Sorry, you've run out of attempts. The word was:", self.secret_word)
                    return "lost"
            elif all(letter in self.guessed_letters for letter in self.secret_word):
                print("Congratulations! You've guessed the word:", self.secret_word)
                return "won"
        else:  # Word guess
            if guess == self.secret_word:
                print("Congratulations! You've guessed the word:", self.secret_word)
                return "won"
            else:
                self.attempts_left -= 1
                print("Incorrect guess. Attempts left:", self.attempts_left)
                if self.attempts_left == 0:
                    print("Sorry, you've run out of attempts. The word was:", self.secret_word)
                    return "lost"

        return "continue"


words_list = ["programming", "python", "Academy", "Knowledge", "Code"]
hangman_game = Hangman(words_list)

print("Welcome to Hangman!")
while True:
    print("Try to guess the word.")
    print("Word:", hangman_game.display_word())

    while True:
        guess = input("Enter a letter or word: ")
        result = hangman_game.guess(guess)
        print("Word:", hangman_game.display_word())

        if result in {"won", "lost"}:
            break
    
    play_again = input("Would you like to play again? (Y/N): ")
    if play_again.lower() != 'y':
        break
    hangman_game = Hangman(words_list)
