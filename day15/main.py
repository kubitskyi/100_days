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
profit = 0

def make_coffe(choice: str):
    drink = MENU[choice]
    ingredients: dict = drink['ingredients']
    cost: float = drink['cost']
    global profit, resources
    
    for k  in ingredients.keys():
        if resources[k] < ingredients[k]:
            return f"Sorry, we don't have a {k.capitalize()}"
     
    for k, v in ingredients.items():
        if resources[k] > v :
            resources[k] -= v
    
    profit += cost
    
    return f"{choice.capitalize()} is done!"

def report()-> str:
    result = ''
    for k, v in resources.items():
        result += f"   - {k.capitalize()} - {v}\n"
    result += f"   - Money - {profit}"
    return result


def main() -> None:
    is_on = True
    while True:
        choise = input("What would you like?: ").lower()
        match choise: 
            case "off":
                print("bye")
                break
            case "report":
                print(report())
            case choise if choise in MENU.keys():
                print(make_coffe(choise))
            case _:
                print("I'm sorry, but I don't understand.")
    
if __name__=="__main__":
    
    main()