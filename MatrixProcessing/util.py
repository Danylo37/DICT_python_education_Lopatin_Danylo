"""Util module"""


def is_digit(u_input):
    """Checking if the user's input is digit (including negative numbers)

    Args:
        u_input (string): user's input

    Returns:
        Boolean True - if u_input is a digit
        Boolean False - if u_input isn't a digit
    """
    if u_input.startswith("-"):
        u_input = u_input[1:]
    return u_input.isdigit()


def get_user_choice(pos_values):
    """Prompts the user for a choice and validates it against a list of possible values.

    Args:
        pos_values (list): list of possible values to choose from

    Returns:
        int: valid user choice selected from possible values
    """
    while True:
        choice = input("Your choice: > ")
        if is_digit(choice) and int(choice) in pos_values:
            return int(choice)
        else:
            print(f"Please enter the value between {pos_values[0]} and {pos_values[len(pos_values)-1]}")
