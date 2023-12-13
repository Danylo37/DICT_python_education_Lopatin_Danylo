"""CoffeeMachine project"""


def positive_int_input():
    """Prompts the user for a positive integer input

    Returns:
        user_input (int): correct user's input (positive integer)
    """

    while True:
        try:
            user_input = int(input("> "))
            if user_input < 0:
                print("Please enter a positive value")
            else:
                return user_input
        except ValueError:
            print("Please enter a positive numeric value")


class CoffeeMachine:
    _espresso_resources = {"water": 250, "milk": 0, "coffee beans": 16, "price": 4}
    _latte_resources = {"water": 350, "milk": 75, "coffee beans": 20, "price": 7}
    _cappuccino_resources = {"water": 200, "milk": 100, "coffee beans": 12, "price": 6}

    def __init__(self):
        self._water = 400
        self._milk = 540
        self._coffee_beans = 120
        self._cups = 9
        self._money = 550

    def _is_enough_resource(self, resources):
        """Check if there are enough resources to make coffee

        Args:
            resources (dictionary): dictionary of the coffee resources
        """

        if self._water < resources.get("water"):
            print("Sorry, not enough water!")

        elif self._milk < resources.get("milk"):
            print("Sorry, not enough milk!")

        elif self._coffee_beans < resources.get("coffee beans"):
            print("Sorry, not enough coffee beans!")

        else:
            print("I have enough resources, making you a coffee!")
            self._water -= resources.get("water")
            self._milk -= resources.get("milk")
            self._coffee_beans -= resources.get("coffee beans")
            self._cups -= 1
            self._money += resources.get("price")

    def _buy(self):
        """Allows user to buy coffee based on selection"""

        if self._cups == 0:
            print("Sorry, but there are no cups left")
            return

        print("What do you want to buy?\n"
              "1 - espresso\n"
              "2 - latte\n"
              "3 - cappuccino\n"
              "back – to main menu")

        while True:
            choice = input("> ")

            if choice == "back":
                return
            elif not choice.isdigit() or int(choice) not in [1, 2, 3]:
                print("Please choose between 1, 2, 3 or \"back\" ")
            else:
                break

        choice = int(choice)

        if choice == 1:  # Espresso
            self._is_enough_resource(self._espresso_resources)

        elif choice == 2:  # Latte
            self._is_enough_resource(self._latte_resources)

        elif choice == 3:  # Cappuccino
            self._is_enough_resource(self._cappuccino_resources)

    def _fill(self):
        """Refills the resources in the coffee machine"""

        print("Write how many ml of water do you want to add:")
        self._water += positive_int_input()

        print("Write how many ml of milk do you want to add:")
        self._milk += positive_int_input()

        print("Write how many grams of coffee beans do you want to add:")
        self._coffee_beans += positive_int_input()

        print("Write how many disposable cups of coffee do you want to add:")
        self._cups += positive_int_input()

    def _take(self):
        """Allows user to take the money from the coffee machine"""

        print(f"I gave you {self._money}")
        self._money = 0

    def _get_remaining(self):
        """Displays the remaining resources in the coffee machine"""

        print(f"The coffee machine has:\n"
              f"{self._water} ml of water\n"
              f"{self._milk} ml of milk\n"
              f"{self._coffee_beans} g of coffee beans\n"
              f"{self._cups} of disposable cups\n"
              f"{self._money} of money")

    def start(self):
        """Starts the coffee machine interaction loop"""

        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input("> ")

            if action == "buy":
                self._buy()

            elif action == "fill":
                self._fill()

            elif action == "take":
                self._take()

            elif action == "remaining":
                self._get_remaining()

            elif action == "exit":
                break


coffee_machine = CoffeeMachine()
coffee_machine.start()
