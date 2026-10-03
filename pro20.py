def Escape_Maze():
    print("Welcome to Escape Maze Game")
    print("You are at Entrance.Choice Left and Right")
    
    choice1=input("Enter Left or Right:  ")
    if choice1=="Left":
        print("You Enter into Dark Tunnel....  ")
        
        choice2=input("Choose Ladder or Door ")
        if choice2=="Ladder":
            print("you climb up and find Exit. You Escaped!   ")
        else:
            print("Door leads to trap Room.Game Over  ")
    
    
    
    elif choice1=="Right":
        print("You Enter a Room with two paths: Forward or Back ")
        
        choice2=input("Choose Forward or Back")
        if choice2=="Forward":
            print("You find a hidden passage leading outside.You Escaped!")
        else:
            print("You return to the Enterence and Get lost.Game Over ")
    
    else:
        print("Invalid Choice.Game over!")
Escape_Maze()        
        
                    