import random 

preffix=["smart","latest","new","best","top","great","amazing","awesome","fantastic","excellent"]
suffix=["hub","world","zone","place","site","space","center","network","community","platform"]

def name_genrator(keyword):
    names=[]
    for i in range(5):
        name=random.choice(preffix)+keyword.capitalize()+random.choice(suffix)
        names.append(name)
    return names

keyword=input("Enter your brand name:   ")
suggestion=name_genrator(keyword)  
print("\n Brand names are :  ")
for s in suggestion:
    print("_",s)  