import random

def Hangman():
    words=["Python","Bedsheet","Computer","PC","Laptop","Cusions"]
    word=random.choice(words)
    gusssed=["_"]*len(word)
    attempts=6
    print("Welcome to Hangman!   ")
    print("Word: "," ".join(gusssed)) 
    
    while attempts > 0 and "_" in gusssed:
        guess=input("Enter a letter:  ") 
             
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    gusssed[i]=guess 
            print("Correct!","".join(gusssed))        
            
        else:
            attempts-=1
            print(f"Wrong! Attempts left:{attempts} ")
    if "_" not in gusssed:
        print("You won. The word was",word)
    else:
        print("Game over!The word was ",word)

Hangman()    
