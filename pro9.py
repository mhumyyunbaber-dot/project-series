import random
units=["rock","paper","scissors"]
PC=random.choice(units)

I=input("rock paper scissors   ").lower()
print("PC choose ",PC )

if I==PC:
    print("Try again")
elif I=="paper" and PC=="scissors":
    print("I won!!")
elif I=="rock" and PC=="Paper":
    print("PC won!!")
elif I=="scissors" and PC=="rock":
    print("PC won!!")
else:
    print("PC won!!")
    