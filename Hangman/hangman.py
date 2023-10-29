"""Hangman project"""
import random

# 1-st stage: Game announcement
print("HANGMAN")

# 3-rd stage: Guessing a random word
words = ["python", "java", "javascript", "php"]
attempts = 8


def word_update(u_letter):
    """Updating hidden word

       Parameters:
       u_letter (string): user's letter

       Returns:
       string: updated hidden word
    """
    for index, letter in enumerate(right_word):
        if letter == u_letter:
            hidden_r_word_letters[index] = u_letter
    return "".join(hidden_r_word_letters)


# 6-th stage: Guessing a random word by letters with more attempts
def is_won():
    """Checking if the user has won

           Returns:
           boolean: True/False
    """
    if "-" not in hidden_r_word_letters and attempts > 0:
        print("You guessed the word!"
              "\nYou survived!")
        return True
    else:
        return False


# 7-th stage: Guessing a word without consuming attempts for repeated letters
guessed_letters = []


def letter_check(u_letter, h_r_word, att):
    """Checking if the user's letter is correct, already guessed or doesn't appear

       Parameters:
       u_letter (string): user's letter
       h_r_word (string): hidden right word
       att (int): count of attempts

       Returns:
       int: count of attempts
    """
    if len(u_letter) != 1:
        print("You should input a single letter.")

    elif not "a" <= u_letter <= "z":
        print("Please enter a lowercase English letter.")

    elif u_letter in h_r_word or u_letter in guessed_letters:
        print("You've already guessed this letter.")

    else:
        print("That letter doesn't appear in the word")
        guessed_letters.append(u_letter)
        return att - 1

    return att


def start_game(att, h_r_word):
    """Starting the game in a loop

       Parameters:
       h_r_word (string): hidden right word
       att (int): count of attempts
    """
    while True:
        print(f"\n{h_r_word}")

        if is_won():
            break

        users_letter = input("Input a letter: > ")

        if users_letter in right_word and users_letter not in h_r_word:
            h_r_word = word_update(users_letter)
        else:
            att = letter_check(users_letter, h_r_word, att)

        if att == 0:
            print("You lost!")
            break


# 8-th stage Starting menu
while True:
    right_word = random.choice(words)
    hidden_r_word_letters = ["-" for i in right_word]
    hidden_r_word = "".join(hidden_r_word_letters)

    play_or_exit = input(r"""Type play to play the game, exit to quit: > """)
    if play_or_exit == "play":
        start_game(attempts, hidden_r_word)
    elif play_or_exit == "exit":
        break
