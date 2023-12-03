"""Pencils game project"""
import random


def get_pencils(p_count):
    """
       Creating a string with the pencils

       Parameters:
       p_count (int): count of pencils

       Returns:
       String: pencils by their count separated by " "
    """
    return " ".join("|" * p_count)


def get_pencil_count():
    """
       Getting initial number of pencils

       Returns:
       p_count (string): count of pencils
    """
    print("How many pencils would you like to use:")
    while True:
        p_count = input("> ")
        if is_digit(p_count):
            p_count = int(p_count)
            if p_count <= 0:
                print("The number of pencils should be positive")
            else:
                return p_count
        else:
            print("The number of pencils should be numeric")


def is_digit(u_input):
    """
       Checking if the user's input is digit (including negative numbers)

       Parameters:
       u_input (string): user's input

       Returns:
       Boolean True - if u_input is a digit
       Boolean False - if u_input isn't a digit
    """
    if u_input.startswith("-"):
        u_input = u_input[1:]
    return u_input.isdigit()


def get_player_pencils():
    """
       Getting number of pencils from the user's input

       Returns:
       player_pencils (int): pencils that takes the user
    """
    while True:
        player_pencils = input("> ")
        if is_digit(player_pencils):
            player_pencils = int(player_pencils)
            if player_pencils > pencil_count:
                print("Too many pencils were taken")
            elif player_pencils not in possible_values:
                print("""Possible values: "1", "2" or "3" """)
            else:
                return player_pencils
        else:
            print("The value should be numeric")


def get_first_player():
    """
       Getting the player who will be the first

       Returns:
       first_player (string): name of the first player
    """
    print("Who will be the first (Mark, John):")
    while True:
        first_player = input("> ")
        if first_player == "Mark" or first_player == "John":
            return first_player
        else:
            print("Choose between \"Mark\" and \"John\"")


def get_bot_pencils(p_count):
    """
       Calculating number of pencils to take for the bot

       Parameters:
       p_count (int): count of pencils

       Returns:
       b_pencils (int): number of pencils that bot takes
    """
    remainder = p_count % 4

    if p_count == 1:       # if the number of pencils is 1
        b_pencils = 1

    elif remainder == 2:   # if the number of pencils is 2, 6, 10, 14...
        b_pencils = 1

    elif remainder == 3:   # if the number of pencils is 3, 7, 11, 15...
        b_pencils = 2

    elif remainder == 0:   # if the number of pencils is 4, 8, 12, 16...
        b_pencils = 3

    else:                  # if the number of pencils is 5, 9, 13, 17...
        b_pencils = random.choice(possible_values)

    print(">", b_pencils)
    return b_pencils


pencil_count = get_pencil_count()
current_player = get_first_player()
possible_values = [1, 2, 3]

while pencil_count != 0:
    # Player moves
    print(get_pencils(pencil_count))
    print(f"{current_player}'s turn!")
    pencil_count -= get_player_pencils()
    current_player = "Mark" if current_player == "John" else "John"

    if pencil_count == 0:
        break

    # Bot moves
    print(get_pencils(pencil_count))
    print(f"{current_player}'s turn!")
    pencil_count -= get_bot_pencils(pencil_count)
    current_player = "Mark" if current_player == "John" else "John"

print(f"{current_player} won!")
