import sys
import time
import os

Level_1 = {
    "What planet is known as the Red Planet?": "Mars",
    "Who invented the telephone?": "Alexander Graham Bell",
    "In Python, what keyword is used to define a function?": "def",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "Which animal is known as the 'Ship of the Desert'?": "Camel",
}

Level_2 = {
    "What is the chemical symbol for gold?": "Au",
    "Which company created the first iPhone?": "Apple inc.",
    "Who was the first person to walk on the moon?": "Neil Armstrong",
    "What does 'HTML' stand for?": "HyperText Markup Language",
    "In which year did World War II end?": "1945",
}

Level_3 = {
    "What is the speed of light in a vacuum (approx) in Km/s?": "299,792Km/s",
    "Who wrote 'The Republic'?": "Plato",
    "What is the main function of a CPU in a computer?": "To process instruction and perform calculations",
    "Which data structure uses FIFO (first in, first out)?": "Queue",
    "Which country gifted the Statue of Liberty to the USA?": "France",
}

Level_4 = {
    "What programming language was developed by Guido van Rossum?": "Python",
    "What is Schrodinger's cat thought experiment about?": "A paradox illustrating quantum superposition the cat is simultaneously alive and dead until observed",
    "Who discovered penicillin?": "Alexander Fleming",
    "What is the Big O notation used for in computer science?": "to describe the efficiency or time complexity of an algorithm",
    "Which philosopher said, 'I think, therefore I am'?": "Rene Descartes"
}


def greet():
    while True:
        Ans = input("\nDo you want to play Quiz Game (yes/no)? ").lower().strip()
        if Ans in ["yes", "y"]:
            return True
        elif Ans in ["no", "n"]:
            print("\nOh, no problem — see you again!")
            return False
        else:
            print("⚠️ Please enter a valid response (yes or no).")


def rules():
    return """
    ------------------------ 🧠 Quiz Game Rules ------------------------
    1. You'll be asked a series of questions across different levels:
       -> Easy, Medium, Hard, and Expert
    2. Type your answer carefully and press Enter to submit
    3. Each correct answer earns you points; wrong answers lose none,
       but you can move ahead after 3 wrong tries.
    4. Once you start a level, you must finish all its questions before
       moving to the next.
    5. Some questions may test speed, others your memory — stay sharp!
    6. You can quit anytime by typing 'exit' or 'no'.
    7. At the end, your final score will decide your title from Rookie
       Thinker to Quiz Master  
    ---------------------------------------------------------------------
    """


def check_level(i):
    return [Level_1, Level_2, Level_3, Level_4][i - 1]


def load():
    print("\nGame starting", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def quit_game():
    print("\nGame quitting", end="", flush=True)
    for _ in range(5):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(0.5)
    clear_screen()
    print("\nGame closed.")
    time.sleep(2)
    sys.exit(0)


def calculating_score(n):
    if 68 <= n <= 100:
        print(f"Rank: Quiz Master 🎯 | Your Score: {n}")
    elif 62 <= n <= 67:
        print(f"Rank: Grand Scholar 🧩 | Your Score: {n}")
    elif 59 <= n <= 61:
        print(f"Rank: Brainiac 🧠 | Your Score: {n}")
    elif 53 <= n <= 58:
        print(f"Rank: Challenger ⚡ | Your Score: {n}")
    elif 47 <= n <= 52:
        print(f"Rank: Rising Mind 🌱 | Your Score: {n}")
    else:
        print(f"Rank: Rookie Thinker 💡 | Your Score: {n}")


def clear_last_lines(n=1):
    for _ in range(n):
        print("\033[F\033[K", end="")
