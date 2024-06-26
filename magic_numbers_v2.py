import random, os, time

MIN_NUMBER = 1
MAX_NUMBER = 10
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
    exit_game()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    global PLAYER_NAME

    print("*"*50, "MAGIC NUMBERS", "*"*50)
    PLAYER_NAME = get_player_name()
    print(f"Hello {PLAYER_NAME}. This is a simple game where I think of a number between {MIN_NUMBER}-{MAX_NUMBER}")
    print("and you have to guess it. You can try 3 times.")
    print("I give you 30 credits to start. If you guess right you win 10 credits.")
    print("Be careful, you could lose all your credits ;)")

def get_player_name():
    return input("What is your name?")

def ask_player(question):
    valid_chars = "yn"
    result = input(f"{question} (y/n)").lower()

    while not result in valid_chars:
        clear_screen()
        print("Wrong answer.")
        result = input(f"{question} (y/n)").lower()

    return result

def game_loop():
    clear_screen()
    global CREDITS

    try_count = 3

    # Get random number between min_number-max_number
    magic_number = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    player_number = get_player_number()

    # check player's number. If wrong ask again.
    while magic_number != player_number:
        clear_screen()
        try_count -= 1
        if try_count == 0:
            break

        print(f"Wrong guess! You have {try_count} tries left. Try again.")
        player_number = get_player_number()

    clear_screen()

    # End game condition
    if magic_number == player_number:
        print(f"You win! {magic_number} was my number! :)")
        print("I give you 10 credits :)")
        CREDITS += 10
    else:
        print(f"You lost the round. My number was {magic_number}.")
        print(f"I take 10 credits from you.")
        CREDITS -= 10
    
    if CREDITS > 0:
        print(f"You have {CREDITS} credits.")
    elif CREDITS == 0:
        print(f"You lost all of your credits but I give you an other chance.")
    else:
        print("You lost all of your credits. Game Over.")

    time.sleep(5)
    clear_screen()

    if CREDITS < 0:
        print("Maybe next time! :)")
    else:
        result = ask_player("Do you want an other round?")
        if result == "y":
            game_loop()
        else:
            exit_game()

def exit_game():
    clear_screen()
    print("Sorry to see you go :( Maybe next time ;)")

def get_player_number():
    return input("What is your guess?")

main()