#This is the starting code for a coffee machine. Enjoy!  

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry, not enough {item}.")
            return False
        else:
            return True

def determine_price(drink1):
    if drink1 == "espresso":
        return 1.5
    elif drink1 == "espresso":
        return 2.5
    else:
        return 3

def calculate_paid():
    print(f"please insert ${price}")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    calc_paid_total = round(
        ((quarters * 0.25)+(dimes * 0.10)+(nickles * 0.05) + (pennies * 0.01)), 2
    )

    return calc_paid_total


is_on = True
money = 100
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
while is_on:
    choice = input("What would you like to drink? Type espresso/latte/cappuccino: ").lower()
    # ToDo 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # ToDo 3. Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml"
              f"\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print("Incorrect selection.  Please try again.")
    # ToDo 4. Check resources sufficient?
    else:
        if check_resources(choice):
            price = determine_price(choice)
            # ToDo 5. Process coins.
            paid = calculate_paid()
            print(f"you have inserted ${paid}")
            # ToDo 6. Check transaction successful?
            if paid < price:
                print("Not enough coins have been inserted.")
                print("Your money has been refunded")
            else:
                if paid > price:
                    refund = round(paid - price, 2)
                    print(f"you have been refunded {refund}")
                money += (paid-refund)
                # ToDo 7. Make Coffee.
                for item in MENU[choice]["ingredients"]:
                    resources[item] -= MENU[choice]["ingredients"][item]
