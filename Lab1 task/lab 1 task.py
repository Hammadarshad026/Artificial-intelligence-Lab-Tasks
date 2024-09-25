import random
import os
class Hangman:
    def __init__(self):
        self.words = ['python', 'Superior', 'Car', 'Rasikh']
        self.word_guess = random.choice(self.words)
        self.correct_letters = set(self.word_guess)
        self.guessed_letters = set()
        self.attempts_left = 6
        
    def display_hangman(self):
        stages = [
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / \\
               |
            ---------
            """,
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / 
               |
            ---------
            """,
            """
               -----
               |   |
               |   O
               |  /|\\
               |  
               |
            ---------
            """,
            """
               -----
               |   |
               |   O
               |  /|
               |  
               |
            ---------
            """,
            """
               -----
               |   |
               |   O
               |   |
               |  
               |
            ---------
            """,
            """
               -----
               |   |
               |   O
               |   
               |  
               |
            ---------
            """,
            """
               -----
               |   |
               |   
               |   
               |  
               |
            ---------
            """,
        ]
        os.system("clear")
        print(stages[self.attempts_left])

    def display_word(self):
        display =[]
        for letter in self.word_guess:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append('_')
        print("Word to guess: " + ' '.join(display))


    def guess_letter(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                if guess in self.guessed_letters:
                    print("You already guessed that letter.")
                else:
                    return guess
            else:
                print("Please enter a single valid letter.")

    def play(self):
        while self.attempts_left > 0:
            self.display_hangman()
            self.display_word()
            guess = self.guess_letter()
            
            if guess in self.correct_letters:
                self.guessed_letters.add(guess)
                print(f"Good job! {guess} is in the word.")
                if self.correct_letters == self.guessed_letters:
                    print("Congratulations! You've guessed the word correctly!")
                    break
            else:
                self.attempts_left -= 1
                print(f"Wrong guess! {guess} is not in the word.")
            
        if self.attempts_left == 0:
            self.display_hangman()
            print(f"Game Over! The word was '{self.word_guess}'.")
game = Hangman()
game.play()
