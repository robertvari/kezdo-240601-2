import random, os, time

PLAYER_NAME = None
CREDITS = 30

def main():
    clear_screen()
    intro()

    time.sleep(5)

    clear_screen()

    result = ask_player(f"Are you ready {PLAYER_NAME}?")
    if result == "y":
        game_loop()
    
    clear_screen()
    print("Sorry to see you go :( Maybe next time ;)")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    global PLAYER_NAME

    print("*"*50, "MAGIC NUMBERS", "*"*50)
    PLAYER_NAME = get_player_name()
    print(f"Hello {PLAYER_NAME}. This is a simple game where I think of a number between 1-10")
    print("and you have to guess it. You can try 3 times.")
    print("I give you 30 credits to start. If you guess right you win 10 credits.")
    print("Be carefull, you could lose all your credits ;)")

def get_player_name():
    return input("What is your name?")

def ask_player(question):
    return input(f"{question} (y/n)").lower()

def game_loop():
    pass

def get_player_number():
    pass

main()