import random

def generate_number():
    number = random.randrange(1, 100)
    return number

def hard():
    user_try = 5
    while user_try > 0:
        user_try = user_try - 1
        user_input = int(input("Guess the Number: "))
        if user_input > number:
            print(f"Too high! {user_try} attempts left")
            print("guess Again..")
        elif user_input < number:
            print(f" Too Low! {user_try} attempts left")
            print("Guess Again..")
        else:
            print(f"Number Matched! Number is {number}")
            print("Game Over!!")
            break

def easy():
    user_try = 10
    while user_try > 0:
        user_try = user_try - 1
        user_input = int(input("Guess the Number: "))
        if user_input > number:
            print(f"Too high! {user_try} attempts left")
            print("guess Again..")
        elif user_input < number:
            print(f" Too Low! {user_try} attempts left")
            print("Guess Again..")
        else:
            print(f"Number Matched! Number is {number}")
            print("Game Over!!")
            break

number = generate_number()
game_mode = input("Choose a difficulty 'easy' or 'hard'")
if game_mode == "easy":
    easy()
else:
    hard()