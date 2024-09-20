import os
import random
os.system("clear")
def fizz_buzz_game():
    flag = True
    while flag:
        n = random.randint(1, 100)
        print(f"Random number generated: {n}")
        user_guess = input("Guess the result (Fizz, Buzz, FizzBuzz, or None): ")
        # os.system("clear")
        if user_guess.upper() == "STOP":
            break
        # n = random.randint(1, 100)
        # print(f"Random number generated: {n}")
        if n % 3 == 0 and n % 5 == 0:
            correct_answer = "Fizz Buzz"
        elif n % 3 == 0:
            correct_answer = "Fizz"
        elif n % 5 == 0:
            correct_answer = "Buzz"
        else:
            correct_answer = "None"
        if user_guess.lower() == correct_answer.lower():
            print(f"Correct! The result is {correct_answer}.")
        else:
            print(f"Wrong! The correct result is {correct_answer}.")
fizz_buzz_game()
