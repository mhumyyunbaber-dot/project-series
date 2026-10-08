def BegDeb():
    print("Welcome to Beginner Debuggig Practice!")
    try:
        num=int(input("Enter a number:   "))
        result=10/num
        print(result)    
    except ZeroDivisionError:
        print("Cannot divided by zero ")
    
    fruits=["apple","banana","peach"]
    
    try:
        index=int(input("Enter the index of fruits:  "))
        print(fruits[index])
    except IndexError:
        print("ERROR:Invalid index")
        
    try:
        age=int(input("Enter Your AGE:   "))
        print(age)
    except ValueError:
               print("ERROR:invalid number is entered")
    
    print("Debuggig Practice is complete")

BegDeb()