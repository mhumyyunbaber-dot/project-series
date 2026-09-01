st=int(input("Enter 1st Number   "))
nd=int(input("Enter 2nd Number   "))
rd=int(input("Enter 3rd Number   "))
rth=int(input("Enter 4rth Number "))

if(st>nd and st>rd and st>rth):
    print(st," is a greatest Number")
elif(nd>st and nd>rd and nd>rth):
    print(nd," is a greatest number")
elif(rd>st and rd>nd and rd>rth):
    print(rd,"is a greatest number")
else:
    print(rth,"is a greatest number")
