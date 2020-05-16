class Coffee:
    water = ""
    milk = ""
    coffee = ""
    cups = ""
    money = ""
    requirement = ()

    def __init__(self, water, milk, coffee, cups, money):
        """
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        """
        self.requirement = (water,
                            milk,
                            coffee,
                            cups,
                            money,
                            )


espresso = Coffee(250, 0, 16, 1, -4)
latte = Coffee(350, 75, 20, 1, -7)
cappuccino = Coffee(200, 100, 12, 1, -6)


class EspressoMachine:
    """
    available_water = 0
    available_milk = 0
    available_coffee = 0
    available_cups = 0
    available_money = 0
    """
    availability = [0,  # available_water
                    0,  # available_milk
                    0,  # available_coffee
                    0,  # available_cups
                    0,  # available_money
                    ]
    availability_name = ("water", "milk", "coffee", "cups")
    state: str = ""

    def __init__(self):
        """
        self.available_water = 400
        self.available_milk = 540
        self.available_coffee = 120
        self.available_cups = 9
        self.available_money = 550
        """
        self.availability = [400,
                             540,
                             120,
                             9,
                             550,
                             ]

    def reduce_availability(self, drink):
        for i in range(5):
            self.availability[i] -= drink.requirement[i]

    def check_availability(self, drink):
        check = []
        for i in range(4):
            check.append(self.availability[i] - drink.requirement[i])
        return min(check) >= 0

    def unavailable(self, drink):
        for i in range(4):
            if self.availability[i] - drink.requirement[i] < 0:
                print(f"Sorry, not enough {self.availability_name[i]}")

    def making_coffee(self):
        if self.state == "":
            self.state = input("Write action (buy, fill, take, remaining, exit): ")

        elif self.state == "buy":
            self.state = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            # return self.state

        elif self.state == "fill":
            for i, k in zip(range(4), ["Write how many ml of water do you want to add: ",
                                       "Write how many ml of milk do you want to add: ",
                                       "Write how many grams of coffee beans do you want to add: ",
                                       "Write how many disposable cups of coffee do you want to add: ",
                                       ]):
                self.availability[i] = int(input(k))
            self.state = ""
            # return self.state

        elif self.state == "take":
            print(f"I gave you ${self.availability[4]}")
            self.availability[4] = 0
            self.state = ""
            # return self.state

        elif self.state == "remaining":
            print("The coffee machine has:")
            for i, k in zip(self.availability, ["of water",
                                                "of milk",
                                                "of coffee beans",
                                                "of disposable cups",
                                                "of money",
                                                ]):
                print(i, k)
            self.state = ""
            # return self.state

        elif self.state == "1":
            if self.check_availability(espresso):
                print("I have enough resources, making you an espresso!")
                self.reduce_availability(espresso)
            else:
                self.unavailable(espresso)
            self.state = ""
            # return self.state

        elif self.state == "2":
            if self.check_availability(latte):
                print("I have enough resources, making you a latte!")
                self.reduce_availability(latte)
            else:
                self.unavailable(espresso)
            self.state = ""
            # return self.state

        elif self.state == "3":
            if self.check_availability(cappuccino):
                print("I have enough resources, making you a cappuccino!")
                self.reduce_availability(cappuccino)
            else:
                self.unavailable(espresso)
            self.state = ""
            # return self.state

        elif self.state == "back":
            self.state = ""
            # return self.state

        elif self.state == "exit":
            return self.state
        else:
            self.state = ""


cm = EspressoMachine()
while True:
    if cm.making_coffee() == 'exit':
        break
