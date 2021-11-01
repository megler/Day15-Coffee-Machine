from recipes import MENU


def coffee_maker():
    QUARTERS = .25
    DIMES = .10
    NICKELS = .05
    PENNIES = .01

    d = {
        "money": 0,
        "coffee": 100,
        "milk": 200,
        "water": 300
    }

    machine_on = True

    def resources(ingredients):

        for order in MENU:
            for item in ingredients:
                if place_order == order and item in MENU[order]["ingredients"]:
                    if MENU[order]["ingredients"][item] >= d[item]:
                        print(f'Sorry, there is not enough {item}.')
                        return False
                    else:
                        d[item] -= MENU[order]["ingredients"][item]
                        return True

    def report():
        print(
            f"    Milk: {d['milk']}ml\n    Water: {d['water']}ml\n    Coffee: {d['coffee']}g\n    Money: {d['money']}")

    def transaction(quarters: int, dimes: int, nickels: int, pennies: int):
        sum = (quarters * QUARTERS) + (dimes * DIMES) + (nickels * NICKELS) + (pennies * PENNIES)

        for drink in MENU:
            if place_order == drink:
                if sum < MENU[drink]["cost"]:
                    print("Sorry that's not enough money. Money refunded")
                    return False
                elif sum > MENU[drink]["cost"]:
                    change = sum - MENU[drink]["cost"]
                    print(f"Here is your ${change:.2f} in change")
                    print(f"Here is your {drink} ☕️. Enjoy!")
                    d['money'] += sum - change
                    return True

    while machine_on:
        place_order = input("What would you like?  (espresso/latte/cappuccino): ")
        if place_order == "off":
            return False
        if place_order == 'report':
            report()
            continue
        if not resources(MENU[place_order]["ingredients"]):
            return False
        print("Please insert coins")
        num_quarters = int(input("How many quarters? "))
        num_dimes = int(input("How many dimes? "))
        num_nickels = int(input("How many nickels? "))
        num_pennies = int(input("How many pennies? "))
        if not transaction(num_quarters, num_dimes, num_nickels, num_pennies):
            return False


coffee_maker()
