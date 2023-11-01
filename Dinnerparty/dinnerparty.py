"""DinnerParty project"""
import random


def update_shares(p_share):
    """Updating people's shares in dictionary

       Parameters:
       int: p_share - person's share
    """
    for p in people:
        if p != lucky_person:
            people[p] = p_share
        else:
            people[p] = 0


def get_num_of_people():
    """Taking user's input and checking if it's correct

       Returns:
       int: user_input - count of people
    """
    while True:
        user_input = input("> ")

        if user_input.isdigit():
            if int(user_input) <= 0:
                print("No one is joining for the party")
                exit()
            else:
                return int(user_input)

        elif user_input == "exit":
            exit()

        else:
            print("Please enter the correct value or \"exit\": > ")


def get_person_share(people_count):
    """Calculating ang rounding person's share

       Parameters:
       int: people_count - count of people

       Returns:
       int: rounded person's share
    """
    return round(total / people_count, 2)


print("Enter the number of friends joining (including you): > ")
num_of_people = get_num_of_people()

people = {}
print("Enter the name of every friend (including you), each on a new line: > ")

for i in range(num_of_people):
    person = input(f"> ")
    people[person] = 0

# 2-nd stage: Division of the total amount
print("Enter the total amount: > ")
total = int(input("> "))
person_share = get_person_share(num_of_people)

for person in people:
    people[person] = person_share

# 3-rd stage: Random selection a lucky person
print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: > ")

# 4-rd stage: Updating the division of the total amount
while True:
    user_answer = input("> ").lower()
    if user_answer == "yes":
        break
    elif user_answer == "no":
        print("No one is going to be lucky")
        print(people)
        exit()
    else:
        print(r"""Please enter "yes" or "no" """)

lucky_person = random.choice(list(people.keys()))
print(f"{lucky_person} is the lucky one!")

new_person_share = get_person_share(num_of_people - 1)
update_shares(new_person_share)

print(people)
