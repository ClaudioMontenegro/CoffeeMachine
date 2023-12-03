from modules import MENU, resources


# also create a constant for keep track of the money we get

profit = 0


def report():
    # alt + shit = select all
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}g")
    print(f"Money: ${profit}")


report()


def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles: ")) * 0.05
    pennies = float(input("how many pennies: ")) * 0.01
    money = quarters + dimes + nickles + pennies
    return money


def make_coffee(answer):
    """Get the input (i.e., the coffee option) and the function coins.
    Check if:
    money are sufficient
    ingredients are sufficient
    then, return the money in change (if necessary)
    Transaction is successful?
    Make the coffee
    """
    if answer == "report":
        # make a report
        return report()
    elif answer == "off":
        # turn off the program
        print("Turn down")
        return False
    global profit
    change = 0
    is_okay = True
    for i in MENU[answer]['ingredients']:
        if resources[i] < MENU[answer]['ingredients'][i]:
            print(f"Sorry there is not enough {i}")
            is_okay = False
    if is_okay:
        money = coins()
        if money >= MENU[answer]['cost']:
            for i in MENU[answer]['ingredients']:
                resources[i] = resources[i] - MENU[answer]['ingredients'][i]
        elif money < MENU[answer]['cost']:
            print(f"Sorry, insufficient money.\nTotal refund: ${money}")
            is_okay = False
        if is_okay:
            change = round(money - MENU[answer]['cost'], 2)
            profit += MENU[answer]['cost']
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {answer} ☕. Enjoy!")
    # report()


would_like = True


while would_like:
    wish = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if make_coffee(wish) is False:
        would_like = False
