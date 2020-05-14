class Coffee:
    water = ""
    milk = ""
    coffee = ""
    cups = ""
    money = ""

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.requirement = (self.water, self.milk, self.coffee, self.cups, self.money)


espresso = Coffee(250, 0, 16, 1, 4)
latte = Coffee(350, 75, 20, 1, 7)
cappuccino = Coffee(200, 100, 12, 1, 6)


class EspressoMachine:
    available_water = 0
    available_milk = 0
    available_coffee = 0
    available_cups = 0
    available_money = 0
    availability = (available_water, available_milk, available_coffee, available_cups, available_money)
    availability_name = ("water", "milk", "coffee", "cups")
    state: str = ""

    def __init__(self):
        self.available_water = 400
        self.available_milk = 540
        self.available_coffee = 120
        self.available_cups = 9
        self.available_money = 550
        self.availability = (self.available_water, self.available_milk, self.available_coffee, self.available_cups, self.available_money)

    def reduce_availability(self, drink):
        for i in range(4):
            self.availability[i] - drink.requirement[i]

    def check_availability(self, drink):
        check = []
        for i in range(4):
            check.append(self.availability[i] - drink.requirement[i])
        return min(check) >= 0

    def unavailable(self, drink):
        for i in range(4):
            if self.availability[i] - drink.requirement[i] < 0:
                print(f"Sorry, not enough{self.availability_name[i]}")

    def making_coffee(self):
        if self.state == "":
            self.state = input("Write action (buy, fill, take, remaining, exit): ")

        if self.state == "buy":
            self.state = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            # return self.state

        if self.state == "fill":
            self.available_water += int(input("Write how many ml of water do you want to add: "))
            self.available_milk += int(input("Write how many ml of milk do you want to add: "))
            self.available_coffee += int(input("Write how many grams of coffee beans do you want to add: "))
            self.available_cups += int(input("Write how many disposable cups of coffee do you want to add: "))
            self.state = ""
            # return self.state

        if self.state == "take":
            print(f"I gave you ${self.available_money}")
            self.available_money = 0
            self.state = ""
            # return self.state

        if self.state == "remaining":
            print("The coffee machine has:")
            print(f"{self.available_water} of water")
            print(f"{self.available_milk} of milk")
            print(f"{self.available_coffee} of coffee beans")
            print(f"{self.available_cups} of disposable cups")
            print(f"${self.available_money} of money")
            self.state = ""
            # return self.state

        if self.state == "1":
            if self.check_availability(espresso):
                print("I have enough resources, making you a coffee!")
                self.reduce_availability(espresso)
                return self.availability
            else:
                self.unavailable(espresso)
            self.state = ""
            # return self.state

        if self.state == "2":
            if self.check_availability(latte):
                print("I have enough resources, making you a coffee!")
                self.reduce_availability(latte)
                return self.availability
            else:
                self.pups(espresso)
            self.state = ""
            # return self.state

        if self.state == "3":
            if self.check_availability(cappuccino):
                print("I have enough resources, making you a coffee!")
                self.reduce_availability(cappuccino)
                return self.availability
            else:
                self.pups(espresso)
            self.state = ""
            # return self.state

        if self.state == "back":
            self.state = ""
            # return self.state

        if self.state == "exit":
            return self.state

while True:
    cm = EspressoMachine()
    if cm.making_coffee() == 'exit':
        break
