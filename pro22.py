def Secret_Auction():
    bids={}
    biding_end=False
    
    print("Welcome to Secret Auction Program! ")
    
    while biding_end==False:
        name=input("Enter bider Name:    ")
        price=int(input("Enter a Bid Amount:  "))
        bids[name]=price

        more_bidder=input("Are there any other Bidder? Type 'yes' or 'No': ").lower()
        
        if more_bidder=="no":
            biding_end=True 
    
    highest_bidder=max(bids, key=bids.get)
    highest_bid=bids[highest_bidder]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
    
Secret_Auction()         