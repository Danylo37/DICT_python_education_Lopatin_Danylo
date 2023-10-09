"""ChatBot project"""

# 1-st stage: Greeting
print("Hello! My name is TestBot. \n"
      "I was created in 2023.")

# 2-nd stage: Entering your name
print("Please, remind me your name.")
name = input("> ")
print(f"What a great name you have, {name}!")

# 3-rd stage: Age guessing
print("Let me guess your age. \n"
      "Enter remainders of dividing your age by 3, 5 and 7:")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

# 4-th stage: Counting from 0 to your number
print("Now I will prove to you that I can count to any number you want.")
num = int(input("> "))
for x in range(num+1):
    print(f"{x} !")

# 5-th stage: Test
print("Let's test your programming knowledge. \n"
      "Why do we use variables in Python?")
print("1. To store and manipulate data. \n"
      "2. To control the flow of a program. \n"
      "3. To create graphical user interfaces. \n"
      "4. To define custom data types.")
while True:
    user_answer = int(input("> "))
    if user_answer == 1:
        print("Completed, have a nice day! \n"
              "Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
