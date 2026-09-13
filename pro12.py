import random
username=input("Enter our Username:  ")
vibes=["its","__ur__","Cool","J@tt","Ar@in", " "]
for i in range(5):
    print(username+random.choice(vibes)+str(random.randint(5,15)))
