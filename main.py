MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# ----------------------------------------------------------- #

# quarter            = $ 0.25
# dime               = $ 0.10
# nickles            = $ 0.05
# penny              = $ 0.01

# ----------------------------------------------------------- #
# GLOBAL VARIABLES

WATER  = 300
MILK   = 200
COFFEE = 100
PROFIT = 0

YOUR_MONEY = 0

# ----------------------------------------------------------- #
# FUNCTIONS

def start_up():
    """The intro screen."""
    print("\nWelcome to the most wonderful coffee machine ever!\nWhat would you like to drink?")
    print("\nEspresso       - $ 1.50 - press [1]")
    print("Latte          - $ 2.50 - press [2]")
    print("Cappuccino     - $ 3.00 - press [3]")
    print("\nFor Maintenance         - press [4]")
    button1 = input("\nChoose and press button: ")
    return button1

def coffee(selected_coffee):
    """After selecting the coffee, this part checks and deducts the necessary ingredients and uses the paying function."""
    global WATER
    global MILK
    global COFFEE
    global YOUR_MONEY
    global PROFIT
    if WATER >= MENU[selected_coffee]["ingredients"]["water"]:
        WATER = WATER - MENU[selected_coffee]["ingredients"]["water"] # this line subtract the necessary amount of water
        if MILK >= MENU[selected_coffee]["ingredients"]["milk"]:
            MILK = MILK - MENU[selected_coffee]["ingredients"]["milk"] # this line subtract the necessary amount of milk
            if COFFEE >= MENU[selected_coffee]["ingredients"]["coffee"]:
                COFFEE = COFFEE - MENU[selected_coffee]["ingredients"]["coffee"] # this line subtract the necessary amount of coffee
                paying()
                if YOUR_MONEY >= MENU[selected_coffee]["cost"]:
                    if YOUR_MONEY > MENU[selected_coffee]["cost"]:
                        print(f"\nHere is ${round(YOUR_MONEY - MENU[selected_coffee]["cost"], 3)} in change. "
                              f"Here is your {selected_coffee}☕. Enjoy!")
                        PROFIT = PROFIT + YOUR_MONEY
                    machine()
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    YOUR_MONEY = 0
            else:
                print("\nSorry, there's not enough coffee.")
                print("\n" * 5)
                machine()
        else:
            print("\nSorry, there's not enough milk.")
            print("\n" * 5)
            machine()
    else:
        print("\nSorry, there's not enough water.")
        print("\n" * 5)
        machine()


def choice1(button1):
    """Let the user choose coffee as an input and start the coffee making function."""
    global WATER
    global MILK
    global COFFEE
    global YOUR_MONEY
    if button1 == "1":
        selected_coffee = "espresso"
        coffee(selected_coffee)
    elif button1 == "2":
        selected_coffee = "latte"
        coffee(selected_coffee)
    elif button1 == "3":
        selected_coffee = "cappuccino"
        coffee(selected_coffee)
    elif button1 == "4":
        maintenance(button1)
    else:
        print("\n" * 20)
        machine()

def maintenance(button1):
    """You print the available resources, refill them, restart of shut down the machine."""
    global WATER
    global MILK
    global COFFEE
    global PROFIT
    print("\nWelcome to the maintenance part of the coffee machine.\nWhat would you like to do?")
    print("\nTo print report         - press [5]")
    print("To refill supplies      - press [6]")
    print("To turn off the machine - press [7]")
    print("To restart the machine  - press [8]")
    button2 = input("\nChoose and press button: ")

    if button2 == "5":
        print(f"\nRemaining water     : {WATER} ml")
        print(f"Remaining milk      : {MILK} ml")
        print(f"Remaining coffee    : {COFFEE} g")
        print(f"The profit          : {PROFIT} $")
        maintenance(button1)
    elif button2 == "6":
        WATER = 300
        MILK = 200
        COFFEE = 100
        maintenance(button1)
    elif button2 == "7":
        print("\nThe system is shutting down.")
        exit()
    elif button2 == "8":
        print("\n" * 20)
        machine()
    else:
        maintenance(button1)

def paying():
    """Asks the user for input in order to pay off the cost of coffee."""
    global YOUR_MONEY
    print("\nPlease insert coins.")

    quarters = int(input("\nHow many quarters ($ 0.25)?: "))
    YOUR_MONEY = round(quarters * 0.25,3)
    print(f"\n<<< You have thrown in ${YOUR_MONEY}. >>>")

    dimes    = int(input("\nHow many dimes    ($ 0.10)?: "))
    YOUR_MONEY = round(YOUR_MONEY + dimes * 0.1,3)
    print(f"\n<<< You have thrown in ${YOUR_MONEY}. >>>")

    nickles  = int(input("\nHow many nickles  ($ 0.05)?: "))
    YOUR_MONEY = round(YOUR_MONEY + nickles * 0.05,3)
    print(f"\n<<< You have thrown in ${YOUR_MONEY}. >>>")

    pennies  = int(input("\nHow many pennies  ($ 0.01)?: "))
    YOUR_MONEY = round(YOUR_MONEY + pennies * 0.01,3)
    print(f"\n<<< You have thrown in ${YOUR_MONEY}. >>>")

    return YOUR_MONEY

def machine():
    """This function is the main system of machine."""
    from art import title
    print(title)
    button1 = start_up()
    choice1(button1)

# ----------------------------------------------------------- #

machine()
