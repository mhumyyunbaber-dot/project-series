import random

def HighLow():
    print("Welcome to hoigher lower game !")
    
    secret_num=random.randint(1,101)
    attempts=7
    
    while attempts>0:
        try:
            guess=int(input("Guess whats the number:   "))
            
        except ValueError:
            print("Out of limit")
            continue
        
        if guess==secret_num:
            print("Congratulations! You gusssed the Right Number")
            break
        elif guess<secret_num:
            print("Number is too low Try again")
        else:
            print("Too hight,TRY Again!")
    
        attempts-=1
        print(f"Attempts left: {attempts}")
    
    if attempts == 0 and guess !=secret_num:
        print(f"Game Over! the number was {secret_num}.")

HighLow()