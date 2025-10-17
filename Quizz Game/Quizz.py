from pyfiglet import Figlet
import sys
import os
import time
from function import greet, rules, check_level, clear_last_lines, load, quit_game, calculating_score


def main():
    score = 0 
    print("Welcome to Quiz Game")
    print("\n---------------")
    if greet() == False:
        quit_game()
    load()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(rules())
    
    for i in range(1, 5):
        print("------------", "Level-", i, "----------------\n")
        Level = check_level(i)
        for index, Question in enumerate(Level, start=1):
            count = 0
            print(f"Q{index}.", Question)
            while True:
                Answer = input("\nAnswer: ")
                if Answer.lower().strip() == Level[Question].lower().strip():
                    print("✅ Correct Answer!")
                    time.sleep(0.5)
                    clear_last_lines(6 if count == 0 else 3)
                    break
                else:
                    clear_last_lines(1 if count == 0 else 3)
                    print("❌ Wrong answer, please try again.")
                    count += 1
                    if count == 3:
                        print("\nAnswer is ->", Level[Question])
                        time.sleep(1)
                        clear_last_lines(5)
                        break
            if count == 0:
                score += 5
            elif count < 3:
                score += 2
        clear_last_lines(2)

    font = Figlet(font='slant')
    calculating_score(score)
    print(font.renderText("Thank You For Playing The Game"))


if __name__ == "__main__":
    main()







