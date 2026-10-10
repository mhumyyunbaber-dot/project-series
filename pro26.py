def CoffeeMachine():
    print("welcome to coffee machine club")
    menu={
        "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
    }
    
    resources={
        "water":300,
        "milk":200,
        "coffee":100
               }
    money=0
    def is_sufficient(order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item]> resources[item]:
                print("Sorry,not Enough item",item)
                return False
        return True
    
    def proccess_coins():
        print("Please Enter Coin")
        quarters=int(input("How many quarters?      "))*0.25
        dimes=int(input("How many dimes?            "))*0.18
        nickles=int(input("How many nickels?        "))*0.05
        pennies=int(input("How many pennis?          "))*0.1
        return quarters+dimes+nickles+pennies
    def make_coffee(drink_name, order_ingredients):
        for item in order_ingredients:
            resources[item]=resources[item]-order_ingredients[item]
        print("Here is your ",drink_name,"☕. Enjoy!")

    while True:
        choice=input("What would you like? (espresso/latte/cappuccino)").lower()
        if choice=="off":
            break
        elif choice=="report":
            print("Resources and Money")
        elif choice in menu:
            drink=menu[choice]
            if is_sufficient(drink["ingredients"]):
                payment=proccess_coins()
                if payment>=drink["cost"]:
                    change=round(payment-drink["cost"],2)
                    if change>0:
                        print(f"Here is your ${change} in change ")                
                    money +=drink["cost"]
                    make_coffee(choice,drink["ingredients"])
                else:
                    print("sorry,not enough money.money refund ")
            else:
                print("Invalid choice")
CoffeeMachine()