import os
import sys
import time
from random import randint


style = "-" * 100
secret = randint(1, 100)
count = 0

def greeting():
    return """
     
    |--------------------------------------------------|
    |          Welcome to Guess Number Game            |
    |        Guess a number between 1 and 100          |
    |               Enter 0 to end game                |
    |                                                  | 
    |--------------------------------------------------| 
    
    """

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    global count, secret, style
    print(greeting())
    print("\n", style)

    while True:
        try:
            raw = input("\n Enter Number: ")
            guess = int(raw)
        except ValueError:
            print("\n Please enter a valid integer between 0 and 100.")
            continue

        print("\n", style)
        count += 1

        if guess == 0:
            print("\n The Secret Number is", secret)
            if ask_play_again():
                secret = get_random()
                count = 0
                restart_animation()
                print(greeting())
                print("\n", style)
                continue
            else:
                quit_game()
        elif guess > secret:
            print("\n Too high!")
        elif guess < secret:
            print("\n Too low!")
        else:
            print("\n 🥳🥳🥳 You guessed right! 🥳🥳🥳")
            if count == 1:
                print(f"\n You guessed the number in {count} try")
            else:
                print(f"\n You guessed the number in {count} tries")
            print("\n", style)
            if ask_play_again():
                secret = get_random()
                count = 0
                restart_animation()
                print(greeting())
                print("\n", style)
                continue
            else:
                quit_game()

def ask_play_again():
    while True:
        ans = input("\n Do you want to play again? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")

def get_random():
    return randint(1, 100)

def quit_game():
    print("\n Game quitting.......", end="", flush=True)
    for _ in range(5):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(0.5)
    clear_screen()
    print("\n Game closed")
    sys.exit(0)

def restart_animation():
    print("\n Restarting.......", end="", flush=True)
    for _ in range(5):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(0.5)
    clear_screen()

if __name__ == '__main__':
    main()