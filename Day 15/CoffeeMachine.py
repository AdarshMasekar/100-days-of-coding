MENU = {
    "coffee" : {
        "ingredients" : {
            "water" : 50,
            "coffee" :18,
    },
    "cost" : 50,
    },
    "cha" : {
        "ingredients" : {
            "water" : 40,
            "cha" :38,
    },
    "cost" : 45,
    },
    "milkshake" : {
        "ingredients" : {
            "milk" : 50,
            "water" :18,
    },
    "cost" : 80,
    },
}

profit = 0

resources = {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100,
    "cha" :90.
}

def is_resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return True

def process_coins():
    """ Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters? : "))* 0.25
    total = int(input("how many dimes? : "))* 0.1
    total = int(input("how many nickles? : "))* 0.05
    total = int(input("how many penniss? : "))* 0.01
    return total

def is_transaction_successfull(money_received, drink_cost):
    """ Returns true when amount is accepted else false"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is a ${change} in change .')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money ")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is Your {drink_name}")


is_on = True
while is_on:
    choice = input("what do you like ? (coffee, cha, milkshake) :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f" water : {resources['water']}ml")
        print(f"Milk :  {resources['milk']}ml")
        print(f"Coffee :  {resources['coffee']}g")
        print(f"cha :  {resources['cha']}g")
        print(f"money : ${profit}")
        
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice ,drink["ingredients"])


    
