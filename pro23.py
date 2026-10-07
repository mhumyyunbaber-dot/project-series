def treasureisland():
    print("Welcome to Treasure Island: ")
    print("Your mission is to find the Treasure on this Island")
    
    choice1=input("Cross Road: Left or Right:  ")
    
    if choice1=="Left":
        choice2=input("Lake:Swim or Wait:  ")
        
        if choice2=="Wait":
            choice3=input("House with door: Red or Yellow or Blue:  ")
            
            if choice3=="Yellow":
                print("You found the treasure.You WON!")
            elif choice3=="Red":
                print("Room of fire,game OVER!")
            elif choice3=="Blue":
                print("Room of Beast.Game over")
            else:        
                print("Invalid Door.Game over!")
        else:
            print("Attacked by Crocodiles.Game OVER")
    else:
        print("Fall into a hole: Game OVER!")
        
treasureisland()