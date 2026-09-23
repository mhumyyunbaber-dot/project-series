Balance=199999
amount=int(input("Enter your Amount you want to withdrawl:  "))
if amount<Balance:
    Balance-=amount
    print("Withdrawl succesfull  ")
    print("Remaining amount",Balance)
else:
    print("Insufficient Amount")