import sys


class Coffee:
    def __init__(self, strength_choice, milk_amount, froth):
        self.strength_choice = strength_choice
        self.milk_amount = milk_amount
        self.froth = froth


class BlackCoffee(Coffee):
    def brew(self, machine):
        coffee_amount = int(self.strength_choice) * 10

        if self.milk_amount + coffee_amount > 200:
            print("Sorry, the cup is too small.")
            return

        # Brew black coffee
        self.milk_amount = 0
        machine.water -= 200 - coffee_amount
        machine.coffee_beans -= coffee_amount

        if machine.milk < 0 or machine.water < 0 or machine.coffee_beans < 0:
            print("Sorry, we don't have enough ingredients for another cup.")
            sys.exit()

        coffee_description = f"A {self.strength_choice}-strength black coffee. Enjoy!"
        print(coffee_description)


class MilkCoffee(Coffee):
    def brew(self, machine):
        if self.milk_amount > machine.milk:
            print("Sorry, we don't have enough milk.")
            return

        coffee_amount = int(self.strength_choice) * 10

        if self.milk_amount + coffee_amount > 200:
            print("Sorry, the cup is too small.")
            return

        # Brew milk coffee
        machine.milk -= self.milk_amount
        machine.water -= 200 - coffee_amount - self.milk_amount
        machine.coffee_beans -= coffee_amount

        if machine.milk < 0 or machine.water < 0 or machine.coffee_beans < 0:
            print("Sorry, we don't have enough ingredients for another cup.")
            sys.exit()

        if self.froth:
            coffee_description = f"A {self.strength_choice}-strength coffee with {self.milk_amount}ml of milk (frothed). Enjoy!"
        else:
            coffee_description = f"A {self.strength_choice}-strength coffee with {self.milk_amount}ml of milk. Enjoy!"
        print(coffee_description)


class CoffeeMachine:
    def __init__(self):
        self.milk = 250
        self.water = 750
        self.coffee_beans = 250

    def make_coffee(self):
        while True:
            self.check_ingredients()  # Notify ingredients before making coffee

            strength_choice = input(
                "What strength of coffee do you want? (1, 2, or 3): ")
            if strength_choice not in ("1", "2", "3"):
                print("Invalid input, please choose 1, 2, or 3.")
                continue

            milk_choice = input("Do you want milk? (y/n): ")
            if milk_choice == "y":
                milk_amount = int(input("How much milk do you want (ml)? "))
                froth_choice = input("Do you want the milk frothed? (y/n): ")
                coffee_type = MilkCoffee(
                    strength_choice, milk_amount, froth_choice == "y")
            else:
                milk_amount = 0
                coffee_type = BlackCoffee(strength_choice, milk_amount, False)

            coffee_type.brew(self)

            continue_choice = input(
                "Do you want to make another coffee? (y/n): ")
            if continue_choice == "n":
                sys.exit()

    def check_ingredients(self):
        print(
            f"We have {self.milk}ml of milk, {self.water}ml of water, and {self.coffee_beans}g of coffee beans left.")


machine = CoffeeMachine()
machine.make_coffee()
