import random, os, platform

def main():
    clear_screen()
    intro()
    
    # get_player_name()
    # ask_player("Are you ready {player_name}?")
    # game_loop()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    print("*"*50, "MAGIC NUMBERS", "*"*50)

def get_player_name():
    pass

def ask_player(question):
    pass

def game_loop():
    pass

def get_player_number():
    pass

main()